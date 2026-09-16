from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import hashlib
import json
import time

import httpx

from .config import Provider, Profile
from .metrics import conservative_request_cost, nominal_cost, usage_from_event


@dataclass
class RunInput:
    run_id: str
    session_id: str
    prompt: str
    context: str
    nonce: str | None

    @property
    def user_content(self) -> str:
        prefix = f"BENCHMARK_RUN_NONCE={self.nonce}\n\n" if self.nonce else ""
        return f"{prefix}{self.prompt}\n\n--- REPOSITORY CONTEXT ---\n{self.context}"


async def run_provider(provider: Provider, profile: Profile, run_input: RunInput, out_dir: Path) -> dict[str, Any]:
    provider_dir = out_dir / provider.name
    provider_dir.mkdir(parents=True, exist_ok=True)
    started = datetime.now(timezone.utc)
    request_body: dict[str, Any] = {
        "model": provider.model,
        "messages": [{"role": "user", "content": run_input.user_content}],
        "stream": True,
        "stream_options": {"include_usage": True},
        "max_tokens": profile.max_output_tokens,
    }
    request_body.update(provider.request_overrides)
    (provider_dir / "request.json").write_text(json.dumps(request_body, ensure_ascii=False, indent=2), encoding="utf-8")

    input_bytes = len(run_input.user_content.encode("utf-8"))
    estimated_cost = conservative_request_cost(provider.pricing, input_bytes, profile.max_output_tokens, started)
    if provider.max_estimated_request_cost is not None and estimated_cost is not None and estimated_cost > provider.max_estimated_request_cost:
        metrics = _base_metrics(provider, run_input, started)
        metrics.update({
            "status": "budget_blocked",
            "estimated_max_request_cost": estimated_cost,
            "max_estimated_request_cost": provider.max_estimated_request_cost,
        })
        _write_metrics(provider_dir, metrics)
        return metrics

    if not provider.api_key:
        metrics = _base_metrics(provider, run_input, started)
        metrics.update({"status": "missing_api_key", "api_key_env": provider.api_key_env})
        _write_metrics(provider_dir, metrics)
        return metrics

    headers = {
        "Authorization": f"Bearer {provider.api_key}",
        "Content-Type": "application/json",
        "Accept": "text/event-stream",
        "User-Agent": profile.user_agent,
    }
    for key, value in provider.headers.items():
        headers[key] = value.format(session_id=run_input.session_id, run_id=run_input.run_id)

    url = f"{provider.base_url}/chat/completions"
    t0 = time.perf_counter_ns()
    first_token_ns: int | None = None
    last_token_ns: int | None = None
    visible_parts: list[str] = []
    reasoning_parts: list[str] = []
    last_usage = {"input_tokens": 0, "cached_input_tokens": 0, "output_tokens": 0, "reasoning_tokens": 0}
    status_code: int | None = None
    finish_reason: str | None = None
    event_count = 0
    raw_path = provider_dir / "stream.jsonl"

    try:
        timeout = httpx.Timeout(profile.timeout_seconds, connect=min(30.0, profile.timeout_seconds))
        async with httpx.AsyncClient(timeout=timeout, http2=True) as client:
            async with client.stream("POST", url, headers=headers, json=request_body) as response:
                status_code = response.status_code
                if response.status_code >= 400:
                    body = (await response.aread()).decode("utf-8", errors="replace")
                    (provider_dir / "error.txt").write_text(body, encoding="utf-8")
                    metrics = _base_metrics(provider, run_input, started)
                    metrics.update({
                        "status": "http_error",
                        "http_status": status_code,
                        "wall_ms": (time.perf_counter_ns() - t0) / 1_000_000,
                        "error_sha256": hashlib.sha256(body.encode()).hexdigest(),
                    })
                    _write_metrics(provider_dir, metrics)
                    return metrics

                with raw_path.open("w", encoding="utf-8") as raw:
                    async for line in response.aiter_lines():
                        if not line.startswith("data:"):
                            continue
                        payload = line[5:].strip()
                        received_ns = time.perf_counter_ns()
                        wall_ns = time.time_ns()
                        if payload == "[DONE]":
                            raw.write(json.dumps({"event_index": event_count, "received_at_unix_ns": wall_ns, "done": True}) + "\n")
                            continue
                        try:
                            data = json.loads(payload)
                        except json.JSONDecodeError:
                            raw.write(json.dumps({"event_index": event_count, "received_at_unix_ns": wall_ns, "raw": payload}) + "\n")
                            event_count += 1
                            continue
                        raw.write(json.dumps({"event_index": event_count, "received_at_unix_ns": wall_ns, "data": data}, ensure_ascii=False) + "\n")
                        event_count += 1
                        if data.get("usage"):
                            last_usage = usage_from_event(data)
                        choices = data.get("choices") or []
                        if not choices:
                            continue
                        choice = choices[0]
                        if choice.get("finish_reason"):
                            finish_reason = str(choice["finish_reason"])
                        delta = choice.get("delta") or {}
                        content = delta.get("content") or ""
                        reasoning = delta.get("reasoning_content") or ""
                        if content or reasoning:
                            if first_token_ns is None:
                                first_token_ns = received_ns
                            last_token_ns = received_ns
                            if content:
                                visible_parts.append(str(content))
                            if reasoning:
                                reasoning_parts.append(str(reasoning))
    except Exception as exc:
        metrics = _base_metrics(provider, run_input, started)
        metrics.update({
            "status": "transport_error",
            "http_status": status_code,
            "wall_ms": (time.perf_counter_ns() - t0) / 1_000_000,
            "error_type": type(exc).__name__,
            "error": str(exc),
        })
        _write_metrics(provider_dir, metrics)
        return metrics

    ended_ns = time.perf_counter_ns()
    visible = "".join(visible_parts)
    reasoning = "".join(reasoning_parts)
    (provider_dir / "response.txt").write_text(visible, encoding="utf-8")
    if reasoning:
        (provider_dir / "reasoning.txt").write_text(reasoning, encoding="utf-8")

    ttft_ms = (first_token_ns - t0) / 1_000_000 if first_token_ns is not None else None
    decode_ms = (last_token_ns - first_token_ns) / 1_000_000 if first_token_ns is not None and last_token_ns is not None else None
    output_tokens = last_usage["output_tokens"]
    tok_s = None
    if decode_ms and decode_ms > 0 and output_tokens > 0:
        tok_s = output_tokens / (decode_ms / 1000.0)

    metrics = _base_metrics(provider, run_input, started)
    metrics.update({
        "status": "ok",
        "http_status": status_code,
        "finish_reason": finish_reason,
        "event_count": event_count,
        "ttft_ms": ttft_ms,
        "decode_ms": decode_ms,
        "wall_ms": (ended_ns - t0) / 1_000_000,
        "decode_tok_sec": tok_s,
        "visible_output_chars": len(visible),
        "reasoning_output_chars": len(reasoning),
        **last_usage,
        "response_sha256": hashlib.sha256(visible.encode("utf-8")).hexdigest(),
        "estimated_max_request_cost": estimated_cost,
        **nominal_cost(provider.pricing, last_usage, started),
    })
    _write_metrics(provider_dir, metrics)
    return metrics


def _base_metrics(provider: Provider, run_input: RunInput, started: datetime) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "run_id": run_input.run_id,
        "started_at": started.isoformat(),
        "provider": provider.name,
        "requested_model": provider.model,
        "billing_mode": provider.billing_mode,
        "balance_hint": provider.balance_hint,
        "prompt_sha256": hashlib.sha256(run_input.prompt.encode("utf-8")).hexdigest(),
        "context_sha256": hashlib.sha256(run_input.context.encode("utf-8")).hexdigest(),
    }


def _write_metrics(provider_dir: Path, metrics: dict[str, Any]) -> None:
    (provider_dir / "metrics.json").write_text(json.dumps(metrics, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
