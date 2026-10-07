# Benchmark statistics

Generated: `2026-10-07T07:17:40+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **106**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 106 | 100% | 1378 ms | 2479 ms | 184.1 | 251.2 | 5.29 s | 8.30 s | 708 | $0.000475 |
| DeepSeek | 106 | 100% | 830 ms | 1163 ms | 237.2 | 257.4 | 3.93 s | 4.87 s | 728 | $0.000486 |
| Fireworks | 106 | 100% | 719 ms | 3050 ms | 95.7 | 179.3 | 8.35 s | 14.02 s | 709 | $0.000530 |
| HAI | 106 | 97% | 3511 ms | 27335 ms | 96.7 | 197.7 | 10.01 s | 95.71 s | 565 | ¥0.1531 |

## Latest run

Run `20261007T071640Z-2c804797` · `2026-10-07T07:16:40.603861+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37586100155)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1434 ms | 124.7 | 6.61 s | 279 | 645 | $0.000858 |
| DeepSeek | ok | stop | 996 ms | 237.5 | 4.42 s | 279 | 813 | $0.001059 |
| Fireworks | ok | stop | 893 ms | 166.1 | 5.60 s | 279 | 781 | $0.000577 |
| HAI | ok | stop | 14978 ms | 12.7 | 59.57 s | 290 | 566 | ¥0.1532 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
