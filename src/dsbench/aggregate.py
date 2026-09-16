from __future__ import annotations

from pathlib import Path
import csv
import json

FIELDS = [
    "run_id", "started_at", "provider", "requested_model", "status", "http_status", "finish_reason",
    "ttft_ms", "decode_ms", "wall_ms", "decode_tok_sec", "input_tokens", "cached_input_tokens",
    "output_tokens", "reasoning_tokens", "currency", "price_window", "nominal_cost", "billing_mode",
    "prompt_sha256", "context_sha256", "response_sha256",
]


def aggregate(results_dir: Path, output: Path) -> int:
    rows = []
    for path in sorted(results_dir.rglob("metrics.json")):
        rows.append(json.loads(path.read_text(encoding="utf-8")))
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return len(rows)
