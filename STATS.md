# Benchmark statistics

Generated: `2026-09-23T20:22:22+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **43**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 43 | 100% | 1146 ms | 1808 ms | 235.3 | 265.6 | 4.36 s | 6.98 s | 710 | $0.000468 |
| DeepSeek | 43 | 100% | 904 ms | 1133 ms | 237.9 | 259.1 | 3.80 s | 4.66 s | 692 | $0.000475 |
| Fireworks | 43 | 100% | 642 ms | 2327 ms | 97.4 | 180.5 | 7.86 s | 10.71 s | 702 | $0.000524 |
| HAI | 43 | 98% | 3018 ms | 29199 ms | 99.8 | 195.7 | 8.69 s | 103.57 s | 532 | ¥0.1451 |

## Latest run

Run `20260923T202156Z-183f031a` · `2026-09-23T20:21:56.707289+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35915414833)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1591 ms | 134.0 | 6.12 s | 280 | 607 | $0.000406 |
| DeepSeek | ok | stop | 556 ms | 235.5 | 3.97 s | 280 | 803 | $0.000524 |
| Fireworks | ok | stop | 448 ms | 96.5 | 8.74 s | 280 | 800 | $0.000590 |
| HAI | ok | stop | 4895 ms | 29.3 | 25.77 s | 291 | 612 | ¥0.1643 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
