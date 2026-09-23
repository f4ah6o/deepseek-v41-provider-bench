# Benchmark statistics

Generated: `2026-09-23T11:36:32+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **41**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 41 | 100% | 1137 ms | 1826 ms | 236.3 | 266.6 | 4.27 s | 7.03 s | 711 | $0.000469 |
| DeepSeek | 41 | 100% | 906 ms | 1137 ms | 237.9 | 259.3 | 3.80 s | 4.67 s | 689 | $0.000475 |
| Fireworks | 41 | 100% | 652 ms | 2384 ms | 99.1 | 181.3 | 7.86 s | 10.76 s | 702 | $0.000524 |
| HAI | 41 | 98% | 2889 ms | 30414 ms | 99.8 | 199.7 | 8.13 s | 104.65 s | 532 | ¥0.1451 |

## Latest run

Run `20260923T113623Z-dbf24f33` · `2026-09-23T11:36:23.445123+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35855491748)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1494 ms | 153.6 | 5.78 s | 286 | 658 | $0.000438 |
| DeepSeek | ok | stop | 754 ms | 229.0 | 3.67 s | 286 | 668 | $0.000444 |
| Fireworks | ok | stop | 2681 ms | 89.0 | 8.27 s | 286 | 498 | $0.000392 |
| HAI | ok | stop | 1948 ms | 154.3 | 5.72 s | 297 | 573 | ¥0.1553 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
