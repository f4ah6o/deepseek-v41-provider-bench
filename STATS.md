# Benchmark statistics

Generated: `2026-09-17T20:21:06+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **8**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 8 | 100% | 1164 ms | 1757 ms | 235.3 | 261.9 | 3.97 s | 7.03 s | 660 | $0.000438 |
| DeepSeek | 8 | 100% | 978 ms | 1179 ms | 237.4 | 251.6 | 4.10 s | 4.68 s | 710 | $0.000476 |
| Fireworks | 8 | 100% | 758 ms | 1982 ms | 108.7 | 171.8 | 7.08 s | 9.14 s | 700 | $0.000523 |
| HAI | 8 | 100% | 2644 ms | 17327 ms | 97.6 | 137.3 | 8.18 s | 74.09 s | 580 | ¥0.1565 |

## Latest run

Run `20260917T202016Z-985ebddc` · `2026-09-17T20:20:16.335644+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35270167356)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1125 ms | 236.3 | 3.66 s | 276 | 589 | $0.000395 |
| DeepSeek | ok | stop | 946 ms | 257.9 | 3.77 s | 276 | 727 | $0.000478 |
| Fireworks | ok | stop | 827 ms | 97.4 | 5.37 s | 276 | 443 | $0.000353 |
| HAI | ok | stop | 4386 ms | 13.6 | 49.63 s | 287 | 617 | ¥0.1653 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
