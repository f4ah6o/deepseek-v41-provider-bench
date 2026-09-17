# Benchmark statistics

Generated: `2026-09-17T23:33:34+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **9**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 9 | 100% | 1146 ms | 1737 ms | 236.3 | 261.1 | 4.07 s | 6.87 s | 668 | $0.000443 |
| DeepSeek | 9 | 100% | 946 ms | 1178 ms | 236.9 | 250.7 | 4.05 s | 4.65 s | 697 | $0.000475 |
| Fireworks | 9 | 100% | 688 ms | 1925 ms | 97.4 | 169.9 | 8.13 s | 9.80 s | 702 | $0.000524 |
| HAI | 9 | 100% | 2433 ms | 16497 ms | 99.4 | 141.6 | 7.62 s | 72.21 s | 543 | ¥0.1476 |

## Latest run

Run `20260917T233324Z-c5f2c26d` · `2026-09-17T23:33:24.150874+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35287348334)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1031 ms | 237.3 | 4.54 s | 281 | 818 | $0.000533 |
| DeepSeek | ok | stop | 668 ms | 236.3 | 2.85 s | 281 | 515 | $0.000351 |
| Fireworks | ok | stop | 682 ms | 85.5 | 10.20 s | 281 | 813 | $0.000598 |
| HAI | ok | stop | 2212 ms | 119.4 | 4.90 s | 292 | 318 | ¥0.0938 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
