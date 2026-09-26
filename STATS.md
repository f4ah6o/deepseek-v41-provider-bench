# Benchmark statistics

Generated: `2026-09-26T17:10:53+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **58**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 58 | 100% | 1210 ms | 2351 ms | 229.3 | 258.0 | 4.49 s | 7.75 s | 710 | $0.000472 |
| DeepSeek | 58 | 100% | 881 ms | 1162 ms | 236.6 | 258.1 | 3.83 s | 4.74 s | 696 | $0.000476 |
| Fireworks | 58 | 100% | 631 ms | 2428 ms | 97.9 | 174.7 | 7.74 s | 11.44 s | 714 | $0.000533 |
| HAI | 58 | 98% | 3447 ms | 28096 ms | 100.2 | 238.8 | 9.78 s | 97.47 s | 547 | ¥0.1487 |

## Latest run

Run `20260926T171038Z-78470df6` · `2026-09-26T17:10:38.863224+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36258072268)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1026 ms | 243.3 | 4.52 s | 278 | 848 | $0.000550 |
| DeepSeek | ok | stop | 691 ms | 251.0 | 2.62 s | 278 | 484 | $0.000332 |
| Fireworks | ok | stop | 656 ms | 70.5 | 13.35 s | 278 | 895 | $0.000652 |
| HAI | ok | stop | 12496 ms | 405.6 | 14.08 s | 289 | 611 | ¥0.1640 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
