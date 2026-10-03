# Benchmark statistics

Generated: `2026-10-03T23:04:22+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **92**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 92 | 100% | 1360 ms | 2374 ms | 187.6 | 250.8 | 5.22 s | 8.16 s | 704 | $0.000469 |
| DeepSeek | 92 | 100% | 833 ms | 1148 ms | 237.1 | 258.5 | 3.87 s | 4.81 s | 708 | $0.000479 |
| Fireworks | 92 | 100% | 693 ms | 2570 ms | 96.1 | 167.3 | 8.32 s | 13.17 s | 712 | $0.000532 |
| HAI | 92 | 97% | 3360 ms | 25936 ms | 100.2 | 197.7 | 9.84 s | 95.32 s | 565 | ¥0.1531 |

## Latest run

Run `20261003T230358Z-ba912f86` · `2026-10-03T23:03:58.632021+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37160525476)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1105 ms | 200.9 | 4.44 s | 282 | 669 | $0.000444 |
| DeepSeek | ok | stop | 594 ms | 216.8 | 2.87 s | 282 | 492 | $0.000338 |
| Fireworks | ok | stop | 1843 ms | 57.3 | 10.04 s | 282 | 470 | $0.000372 |
| HAI | ok | stop | 4796 ms | 28.1 | 23.17 s | 293 | 514 | ¥0.1409 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
