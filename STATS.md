# Benchmark statistics

Generated: `2026-10-09T02:11:18+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **113**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 113 | 100% | 1374 ms | 2617 ms | 178.4 | 250.7 | 5.31 s | 8.13 s | 704 | $0.000476 |
| DeepSeek | 113 | 100% | 834 ms | 1172 ms | 237.2 | 256.8 | 3.93 s | 4.84 s | 727 | $0.000488 |
| Fireworks | 113 | 100% | 706 ms | 2878 ms | 96.5 | 183.2 | 8.13 s | 13.88 s | 706 | $0.000528 |
| HAI | 113 | 97% | 3565 ms | 27997 ms | 95.8 | 197.6 | 10.79 s | 100.31 s | 573 | ¥0.1550 |

## Latest run

Run `20261009T020949Z-a9cc2276` · `2026-10-09T02:09:49.767125+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37873236970)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1326 ms | 133.1 | 5.93 s | 284 | 612 | $0.000820 |
| DeepSeek | ok | stop | 847 ms | 219.5 | 4.56 s | 284 | 815 | $0.001063 |
| Fireworks | ok | stop | 1241 ms | 230.9 | 3.39 s | 284 | 495 | $0.000389 |
| HAI | ok | stop | 3617 ms | 9.1 | 88.98 s | 295 | 772 | ¥0.2030 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
