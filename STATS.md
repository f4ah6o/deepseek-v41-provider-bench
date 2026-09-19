# Benchmark statistics

Generated: `2026-09-19T20:40:22+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **20**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 20 | 100% | 1141 ms | 1511 ms | 238.8 | 266.7 | 4.13 s | 6.60 s | 689 | $0.000455 |
| DeepSeek | 20 | 100% | 941 ms | 1164 ms | 238.7 | 258.0 | 3.79 s | 4.93 s | 690 | $0.000466 |
| Fireworks | 20 | 100% | 689 ms | 2550 ms | 97.3 | 154.5 | 8.24 s | 11.31 s | 720 | $0.000537 |
| HAI | 20 | 95% | 2482 ms | 23751 ms | 99.4 | 220.5 | 7.58 s | 87.99 s | 543 | ¥0.1476 |

## Latest run

Run `20260919T204013Z-f2d9b663` · `2026-09-19T20:40:13.916280+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35468087409)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1089 ms | 246.5 | 3.61 s | 280 | 620 | $0.000414 |
| DeepSeek | ok | stop | 868 ms | 243.1 | 3.19 s | 280 | 564 | $0.000380 |
| Fireworks | ok | stop | 586 ms | 93.5 | 8.54 s | 280 | 743 | $0.000552 |
| HAI | ok | stop | 3447 ms | 425.1 | 4.21 s | 291 | 316 | ¥0.0933 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
