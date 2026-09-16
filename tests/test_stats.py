from pathlib import Path
import csv

from dsbench.stats import pct, record


def test_percentile_linear_interpolation():
    assert pct([1.0, 2.0, 3.0, 4.0], 0.5) == 2.5
    assert pct([10.0], 0.95) == 10.0
    assert pct([], 0.95) is None


def test_record_deduplicates_and_renders(tmp_path: Path):
    metrics = tmp_path / "metrics.csv"
    with metrics.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["run_id", "started_at", "provider", "status", "ttft_ms", "decode_tok_sec", "wall_ms", "output_tokens", "currency", "nominal_cost"])
        writer.writeheader()
        writer.writerow({"run_id": "r1", "started_at": "2026-09-16T00:00:00+00:00", "provider": "deepseek", "status": "ok", "ttft_ms": "100", "decode_tok_sec": "200", "wall_ms": "1000", "output_tokens": "500", "currency": "USD", "nominal_cost": "0.001"})
    history, summary = tmp_path / "data/history.csv", tmp_path / "STATS.md"
    for _ in range(2):
        assert record(metrics, history, summary, "repo-review", 4096, "123", "https://example/run/123") == 1
    rows = list(csv.DictReader(history.open(newline="", encoding="utf-8")))
    assert len(rows) == 1
    text = summary.read_text(encoding="utf-8")
    assert "Current profile: **`repo-review`**" in text
    assert "DeepSeek" in text and "200.0" in text and "GitHub Actions" in text
