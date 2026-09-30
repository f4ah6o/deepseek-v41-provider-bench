# Benchmark statistics

Generated: `2026-09-30T13:44:30+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **76**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 76 | 100% | 1332 ms | 1961 ms | 217.4 | 252.7 | 5.01 s | 8.06 s | 708 | $0.000469 |
| DeepSeek | 76 | 100% | 874 ms | 1143 ms | 236.9 | 256.5 | 3.87 s | 4.69 s | 718 | $0.000481 |
| Fireworks | 76 | 100% | 666 ms | 2407 ms | 96.8 | 169.8 | 7.93 s | 12.81 s | 712 | $0.000532 |
| HAI | 76 | 97% | 3404 ms | 27926 ms | 100.1 | 211.5 | 9.47 s | 98.69 s | 560 | ¥0.1520 |

## Latest run

Run `20260930T134321Z-44320a40` · `2026-09-30T13:43:21.681418+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36723690037)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1335 ms | 158.4 | 6.82 s | 279 | 868 | $0.000563 |
| DeepSeek | ok | stop | 689 ms | 235.4 | 3.97 s | 279 | 771 | $0.000504 |
| Fireworks | ok | stop | 702 ms | 90.7 | 8.73 s | 279 | 728 | $0.000542 |
| HAI | ok | stop | 4404 ms | 11.4 | 68.89 s | 290 | 732 | ¥0.1931 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
