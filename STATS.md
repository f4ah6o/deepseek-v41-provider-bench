# Benchmark statistics

Generated: `2026-09-20T06:16:19+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **23**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 23 | 100% | 1178 ms | 1488 ms | 238.8 | 266.7 | 4.19 s | 6.38 s | 689 | $0.000455 |
| DeepSeek | 23 | 100% | 941 ms | 1157 ms | 237.4 | 257.4 | 3.86 s | 4.86 s | 692 | $0.000475 |
| Fireworks | 23 | 100% | 689 ms | 2327 ms | 97.4 | 152.3 | 8.13 s | 11.15 s | 702 | $0.000524 |
| HAI | 23 | 96% | 2457 ms | 22808 ms | 100.9 | 235.0 | 7.15 s | 86.24 s | 532 | ¥0.1451 |

## Latest run

Run `20260920T061613Z-74583ca1` · `2026-09-20T06:16:13.949750+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35493783233)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1284 ms | 229.2 | 5.04 s | 283 | 859 | $0.000558 |
| DeepSeek | ok | stop | 952 ms | 231.0 | 3.86 s | 283 | 671 | $0.000445 |
| Fireworks | ok | stop | 548 ms | 121.3 | 5.66 s | 283 | 620 | $0.000471 |
| HAI | ok | stop | 1608 ms | 119.9 | 5.11 s | 294 | 416 | ¥0.1175 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
