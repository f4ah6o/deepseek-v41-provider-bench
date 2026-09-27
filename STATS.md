# Benchmark statistics

Generated: `2026-09-27T01:27:36+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **61**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 61 | 100% | 1233 ms | 2125 ms | 227.3 | 256.4 | 4.54 s | 7.72 s | 710 | $0.000468 |
| DeepSeek | 61 | 100% | 881 ms | 1162 ms | 237.3 | 257.9 | 3.82 s | 4.72 s | 700 | $0.000477 |
| Fireworks | 61 | 100% | 642 ms | 2384 ms | 97.4 | 173.5 | 7.67 s | 12.85 s | 706 | $0.000528 |
| HAI | 61 | 98% | 3404 ms | 27875 ms | 100.9 | 237.4 | 9.42 s | 96.24 s | 552 | ¥0.1498 |

## Latest run

Run `20260927T012728Z-9a43c098` · `2026-09-27T01:27:28.908280+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36285574853)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1337 ms | 133.1 | 6.55 s | 277 | 693 | $0.000457 |
| DeepSeek | ok | stop | 819 ms | 252.6 | 3.82 s | 277 | 757 | $0.000496 |
| Fireworks | ok | stop | 677 ms | 89.7 | 7.48 s | 277 | 610 | $0.000464 |
| HAI | ok | stop | 2165 ms | 148.9 | 5.34 s | 288 | 468 | ¥0.1296 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
