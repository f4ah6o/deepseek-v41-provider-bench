# Benchmark statistics

Generated: `2026-09-19T14:25:33+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **18**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 18 | 100% | 1141 ms | 1552 ms | 236.8 | 266.8 | 4.13 s | 6.79 s | 689 | $0.000455 |
| DeepSeek | 18 | 100% | 943 ms | 1167 ms | 238.7 | 258.1 | 3.79 s | 4.99 s | 690 | $0.000466 |
| Fireworks | 18 | 100% | 689 ms | 2884 ms | 97.3 | 157.7 | 8.24 s | 11.53 s | 720 | $0.000537 |
| HAI | 18 | 94% | 2482 ms | 24364 ms | 95.8 | 164.7 | 7.62 s | 88.72 s | 545 | ¥0.1483 |

## Latest run

Run `20260919T142524Z-914ee09c` · `2026-09-19T14:25:24.669357+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35448676528)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1178 ms | 229.4 | 4.57 s | 279 | 774 | $0.000506 |
| DeepSeek | ok | stop | 769 ms | 259.3 | 3.41 s | 279 | 683 | $0.000452 |
| Fireworks | ok | stop | 737 ms | 88.2 | 8.35 s | 279 | 672 | $0.000505 |
| HAI | ok | stop | 2482 ms | 120.6 | 6.97 s | 290 | 541 | ¥0.1472 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
