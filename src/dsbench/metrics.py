from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


def is_peak(pricing: dict[str, Any], when: datetime) -> bool:
    windows = pricing.get("weekday_peak_windows_utc") or []
    if not windows:
        return False
    utc = when.astimezone(timezone.utc)
    if utc.weekday() >= 5:
        return False
    minute = utc.hour * 60 + utc.minute
    for window in windows:
        start_s, end_s = window.split("-", 1)
        sh, sm = map(int, start_s.split(":"))
        eh, em = map(int, end_s.split(":"))
        start, end = sh * 60 + sm, eh * 60 + em
        if start <= minute < end:
            return True
    return False


def price_rates(pricing: dict[str, Any], when: datetime) -> tuple[str | None, dict[str, float] | None, str]:
    currency = pricing.get("currency")
    if "fixed" in pricing:
        return currency, dict(pricing["fixed"]), "fixed"
    if "peak" in pricing and "offpeak" in pricing:
        peak = is_peak(pricing, when)
        return currency, dict(pricing["peak" if peak else "offpeak"]), "peak" if peak else "offpeak"
    return currency, None, "unknown"


def usage_from_event(data: dict[str, Any]) -> dict[str, int]:
    usage = data.get("usage") or {}
    prompt = usage.get("prompt_tokens", usage.get("input_tokens", 0)) or 0
    completion = usage.get("completion_tokens", usage.get("output_tokens", 0)) or 0
    details = usage.get("prompt_tokens_details") or usage.get("input_tokens_details") or {}
    cached = details.get("cached_tokens", details.get("cached_input_tokens", 0)) or 0
    reasoning_details = usage.get("completion_tokens_details") or usage.get("output_tokens_details") or {}
    reasoning = reasoning_details.get("reasoning_tokens", 0) or 0
    return {
        "input_tokens": int(prompt),
        "cached_input_tokens": int(cached),
        "output_tokens": int(completion),
        "reasoning_tokens": int(reasoning),
    }


def nominal_cost(pricing: dict[str, Any], usage: dict[str, int], when: datetime) -> dict[str, Any]:
    currency, rates, price_window = price_rates(pricing, when)
    if not rates:
        return {"currency": currency, "price_window": price_window, "nominal_cost": None}
    total_input = usage.get("input_tokens", 0)
    cached = min(total_input, usage.get("cached_input_tokens", 0))
    miss = max(0, total_input - cached)
    cost = (
        miss * float(rates.get("input_miss", 0.0))
        + cached * float(rates.get("input_cache", rates.get("input_miss", 0.0)))
        + usage.get("output_tokens", 0) * float(rates.get("output", 0.0))
    ) / 1_000_000
    return {"currency": currency, "price_window": price_window, "nominal_cost": cost}


def conservative_request_cost(pricing: dict[str, Any], input_bytes: int, max_output_tokens: int, when: datetime) -> float | None:
    _, rates, _ = price_rates(pricing, when)
    if not rates:
        return None
    estimated_input_tokens = max(1, (input_bytes + 2) // 3)
    return (
        estimated_input_tokens * float(rates.get("input_miss", 0.0))
        + max_output_tokens * float(rates.get("output", 0.0))
    ) / 1_000_000
