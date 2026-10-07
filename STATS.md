# Benchmark statistics

Generated: `2026-10-07T20:38:05+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **108**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 108 | 100% | 1374 ms | 2444 ms | 182.7 | 251.0 | 5.29 s | 8.25 s | 704 | $0.000471 |
| DeepSeek | 108 | 100% | 833 ms | 1176 ms | 237.2 | 257.3 | 3.93 s | 4.86 s | 728 | $0.000486 |
| Fireworks | 108 | 100% | 712 ms | 3001 ms | 96.1 | 178.5 | 8.32 s | 13.98 s | 708 | $0.000529 |
| HAI | 108 | 97% | 3534 ms | 28086 ms | 96.6 | 197.6 | 10.17 s | 102.35 s | 565 | ¥0.1531 |

## Latest run

Run `20261007T203731Z-948ec1d7` · `2026-10-07T20:37:31.443072+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37683405286)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1178 ms | 171.0 | 4.84 s | 280 | 626 | $0.000418 |
| DeepSeek | ok | stop | 1030 ms | 239.0 | 3.91 s | 280 | 686 | $0.000454 |
| Fireworks | ok | stop | 509 ms | 140.9 | 4.65 s | 280 | 583 | $0.000446 |
| HAI | ok | stop | 3771 ms | 25.9 | 33.97 s | 291 | 782 | ¥0.2051 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
