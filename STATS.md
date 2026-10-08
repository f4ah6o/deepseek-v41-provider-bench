# Benchmark statistics

Generated: `2026-10-08T15:37:32+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **111**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 111 | 100% | 1375 ms | 2629 ms | 182.1 | 250.9 | 5.31 s | 8.18 s | 705 | $0.000476 |
| DeepSeek | 111 | 100% | 834 ms | 1174 ms | 237.2 | 257.0 | 3.93 s | 4.85 s | 727 | $0.000488 |
| Fireworks | 111 | 100% | 702 ms | 2927 ms | 96.3 | 181.6 | 8.27 s | 13.92 s | 706 | $0.000528 |
| HAI | 111 | 97% | 3565 ms | 28033 ms | 95.8 | 197.6 | 10.79 s | 101.13 s | 570 | ¥0.1540 |

## Latest run

Run `20261008T153658Z-168f086e` · `2026-10-08T15:36:58.339020+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37802182425)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 881 ms | 143.6 | 6.41 s | 276 | 793 | $0.000517 |
| DeepSeek | ok | stop | 849 ms | 246.0 | 3.29 s | 276 | 599 | $0.000401 |
| Fireworks | ok | stop | 434 ms | 181.9 | 4.99 s | 276 | 829 | $0.000608 |
| HAI | ok | stop | 10272 ms | 24.7 | 33.57 s | 287 | 573 | ¥0.1547 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
