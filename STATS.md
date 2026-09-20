# Benchmark statistics

Generated: `2026-09-20T21:33:44+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **27**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 27 | 100% | 1146 ms | 1482 ms | 238.8 | 266.7 | 4.19 s | 6.17 s | 691 | $0.000456 |
| DeepSeek | 27 | 100% | 906 ms | 1145 ms | 237.9 | 257.0 | 3.87 s | 4.79 s | 697 | $0.000477 |
| Fireworks | 27 | 100% | 688 ms | 2215 ms | 99.1 | 151.0 | 8.13 s | 11.07 s | 702 | $0.000524 |
| HAI | 27 | 96% | 3151 ms | 28905 ms | 97.6 | 227.2 | 7.60 s | 111.69 s | 532 | ¥0.1451 |

## Latest run

Run `20260920T213316Z-ee8a7c1c` · `2026-09-20T21:33:16.273114+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35539054699)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 972 ms | 244.1 | 4.18 s | 281 | 770 | $0.000504 |
| DeepSeek | ok | stop | 565 ms | 222.7 | 3.87 s | 281 | 736 | $0.000484 |
| Fireworks | ok | stop | 377 ms | 92.4 | 8.34 s | 281 | 736 | $0.000548 |
| HAI | ok | stop | 6499 ms | 22.6 | 27.86 s | 292 | 479 | ¥0.1325 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
