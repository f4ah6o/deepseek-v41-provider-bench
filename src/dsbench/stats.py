from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import argparse
import csv
import math

FIELDS = [
    "profile", "max_output_tokens", "github_run_id", "github_run_url",
    "run_id", "started_at", "provider", "requested_model", "status",
    "http_status", "finish_reason", "ttft_ms", "decode_ms", "wall_ms",
    "decode_tok_sec", "input_tokens", "cached_input_tokens", "output_tokens",
    "reasoning_tokens", "currency", "price_window", "nominal_cost", "billing_mode",
]
NAMES = {"opencode_go": "OpenCode Go", "deepseek": "DeepSeek", "fireworks": "Fireworks", "hai": "HAI"}
ORDER = ["opencode_go", "deepseek", "fireworks", "hai"]


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in FIELDS})


def num(value: str | None) -> float | None:
    if value in (None, ""):
        return None
    try:
        result = float(value)
    except (TypeError, ValueError):
        return None
    return result if math.isfinite(result) else None


def values(rows: list[dict[str, str]], field: str) -> list[float]:
    return [v for row in rows if (v := num(row.get(field))) is not None]


def pct(items: list[float], q: float) -> float | None:
    if not items:
        return None
    items = sorted(items)
    if len(items) == 1:
        return items[0]
    pos = (len(items) - 1) * q
    lo, hi = math.floor(pos), math.ceil(pos)
    return items[lo] if lo == hi else items[lo] + (items[hi] - items[lo]) * (pos - lo)


def provider_key(name: str) -> tuple[int, str]:
    return (ORDER.index(name), name) if name in ORDER else (len(ORDER), name)


def ms(value: float | None) -> str:
    return "—" if value is None else f"{value:.0f} ms"


def sec(value: float | None) -> str:
    return "—" if value is None else f"{value / 1000:.2f} s"


def rate(value: float | None) -> str:
    return "—" if value is None else f"{value:.1f}"


def integer(value: float | None) -> str:
    return "—" if value is None else f"{value:.0f}"


def cost(value: float | None, currency: str) -> str:
    if value is None:
        return "—"
    if currency == "USD":
        return f"${value:.6f}"
    if currency == "JPY":
        return f"¥{value:.4f}"
    return f"{value:.6f} {currency}".strip()


def render(history: list[dict[str, str]], profile: str) -> str:
    rows = [row for row in history if row.get("profile") == profile]
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    out = ["# Benchmark statistics", "", f"Generated: `{now}`", ""]
    if not rows:
        return "\n".join(out + [f"No samples recorded for profile `{profile}` yet.", ""])

    latest_row = max(rows, key=lambda row: row.get("started_at", ""))
    runs = {row.get("run_id", "") for row in rows if row.get("run_id")}
    out += [
        f"Current profile: **`{profile}`** · max output: **{latest_row.get('max_output_tokens', 'unknown')} tokens** · runs: **{len(runs)}**",
        "",
        "Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.",
        "",
        "## Provider summary", "",
        "| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    providers = sorted({row["provider"] for row in rows}, key=provider_key)
    for provider in providers:
        sample = [row for row in rows if row["provider"] == provider]
        ok = [row for row in sample if row.get("status") == "ok"]
        currency = next((row.get("currency", "") for row in reversed(ok) if row.get("currency")), "")
        cols = [
            NAMES.get(provider, provider), str(len(sample)), f"{100 * len(ok) / len(sample):.0f}%",
            ms(pct(values(ok, "ttft_ms"), .5)), ms(pct(values(ok, "ttft_ms"), .95)),
            rate(pct(values(ok, "decode_tok_sec"), .5)), rate(pct(values(ok, "decode_tok_sec"), .95)),
            sec(pct(values(ok, "wall_ms"), .5)), sec(pct(values(ok, "wall_ms"), .95)),
            integer(pct(values(ok, "output_tokens"), .5)), cost(pct(values(ok, "nominal_cost"), .5), currency),
        ]
        out.append("| " + " | ".join(cols) + " |")

    latest_id = latest_row["run_id"]
    latest = [row for row in rows if row.get("run_id") == latest_id]
    started = min(row.get("started_at", "") for row in latest)
    url = next((row.get("github_run_url", "") for row in latest if row.get("github_run_url")), "")
    label = f"Run `{latest_id}` · `{started}`" + (f" · [GitHub Actions]({url})" if url else "")
    out += ["", "## Latest run", "", label, "",
            "| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |",
            "| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |"]
    for row in sorted(latest, key=lambda r: provider_key(r.get("provider", ""))):
        cols = [
            NAMES.get(row.get("provider", ""), row.get("provider", "")), row.get("status", ""), row.get("finish_reason", "") or "—",
            ms(num(row.get("ttft_ms"))), rate(num(row.get("decode_tok_sec"))), sec(num(row.get("wall_ms"))),
            row.get("input_tokens", "") or "—", row.get("output_tokens", "") or "—",
            cost(num(row.get("nominal_cost")), row.get("currency", "")),
        ]
        out.append("| " + " | ".join(cols) + " |")

    out += [
        "", "## Notes", "",
        "- p50 is the median. p95 uses linear interpolation over successful samples.",
        "- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.",
        "- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.",
        "- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.",
        "- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.", "",
    ]
    return "\n".join(out)


def record(metrics: Path, history_path: Path, output: Path, profile: str, max_tokens: int, run_id: str = "", run_url: str = "") -> int:
    incoming = read_csv(metrics)
    if not incoming:
        return 0
    current = read_csv(history_path)
    keyed = {(r.get("profile", ""), r.get("run_id", ""), r.get("provider", "")): r for r in current}
    for row in incoming:
        item = {key: row.get(key, "") for key in FIELDS}
        item.update(profile=profile, max_output_tokens=str(max_tokens), github_run_id=run_id, github_run_url=run_url)
        keyed[(profile, item["run_id"], item["provider"])] = item
    history = sorted(keyed.values(), key=lambda r: (r.get("started_at", ""), r.get("run_id", ""), r.get("provider", "")))
    write_csv(history_path, history)
    output.write_text(render(history, profile), encoding="utf-8")
    return len(incoming)


def main() -> None:
    from .config import load_config
    parser = argparse.ArgumentParser(prog="python -m dsbench.stats")
    parser.add_argument("--config", default="benchmark.yaml")
    parser.add_argument("--metrics", default="results/hourly.csv")
    parser.add_argument("--history", default="data/history.csv")
    parser.add_argument("--output", default="STATS.md")
    parser.add_argument("--github-run-id", default="")
    parser.add_argument("--github-run-url", default="")
    args = parser.parse_args()
    cfg = load_config(args.config)
    count = record(Path(args.metrics), Path(args.history), Path(args.output), cfg.profile.name, cfg.profile.max_output_tokens, args.github_run_id, args.github_run_url)
    print(f"recorded {count} benchmark rows")


if __name__ == "__main__":
    main()
