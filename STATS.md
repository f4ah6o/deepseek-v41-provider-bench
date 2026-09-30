# Benchmark statistics

Generated: `2026-09-30T00:27:14+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **74**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 74 | 100% | 1333 ms | 1982 ms | 217.4 | 253.2 | 4.88 s | 8.11 s | 704 | $0.000468 |
| DeepSeek | 74 | 100% | 881 ms | 1146 ms | 236.9 | 256.7 | 3.87 s | 4.70 s | 718 | $0.000480 |
| Fireworks | 74 | 100% | 654 ms | 2417 ms | 96.8 | 170.3 | 7.84 s | 12.81 s | 708 | $0.000529 |
| HAI | 74 | 97% | 3237 ms | 25236 ms | 100.2 | 215.4 | 9.12 s | 95.13 s | 552 | ¥0.1498 |

## Latest run

Run `20260930T002707Z-d5582bb4` · `2026-09-30T00:27:07.235569+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36650383035)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1694 ms | 149.9 | 6.36 s | 279 | 699 | $0.000461 |
| DeepSeek | ok | stop | 819 ms | 211.5 | 3.70 s | 279 | 608 | $0.000407 |
| Fireworks | ok | stop | 849 ms | 157.1 | 4.90 s | 279 | 636 | $0.000481 |
| HAI | ok | stop | 2291 ms | 93.9 | 6.70 s | 290 | 411 | ¥0.1160 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
