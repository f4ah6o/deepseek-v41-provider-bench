# Benchmark statistics

Generated: `2026-09-26T22:50:28+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **60**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 60 | 100% | 1223 ms | 2201 ms | 228.2 | 256.9 | 4.53 s | 7.73 s | 710 | $0.000469 |
| DeepSeek | 60 | 100% | 881 ms | 1162 ms | 237.1 | 258.0 | 3.83 s | 4.73 s | 698 | $0.000476 |
| Fireworks | 60 | 100% | 631 ms | 2398 ms | 97.9 | 173.9 | 7.74 s | 12.85 s | 708 | $0.000529 |
| HAI | 60 | 98% | 3447 ms | 27948 ms | 100.2 | 237.9 | 9.78 s | 96.65 s | 556 | ¥0.1509 |

## Latest run

Run `20260926T225022Z-ed985ebf` · `2026-09-26T22:50:22.895481+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36277548458)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1351 ms | 159.4 | 4.78 s | 280 | 546 | $0.000370 |
| DeepSeek | ok | stop | 692 ms | 243.6 | 3.64 s | 280 | 714 | $0.000470 |
| Fireworks | ok | stop | 316 ms | 150.8 | 4.39 s | 280 | 614 | $0.000467 |
| HAI | ok | stop | 1766 ms | 196.9 | 5.08 s | 291 | 645 | ¥0.1723 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
