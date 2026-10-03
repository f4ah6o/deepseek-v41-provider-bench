# Benchmark statistics

Generated: `2026-10-03T12:33:55+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **89**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 89 | 100% | 1351 ms | 2389 ms | 185.3 | 251.0 | 5.25 s | 8.23 s | 710 | $0.000476 |
| DeepSeek | 89 | 100% | 845 ms | 1152 ms | 237.0 | 255.9 | 3.89 s | 4.81 s | 719 | $0.000481 |
| Fireworks | 89 | 100% | 688 ms | 2601 ms | 96.3 | 167.7 | 8.27 s | 13.22 s | 720 | $0.000536 |
| HAI | 89 | 97% | 3342 ms | 26635 ms | 100.2 | 197.7 | 9.81 s | 95.51 s | 569 | ¥0.1542 |

## Latest run

Run `20261003T123340Z-eccfc396` · `2026-10-03T12:33:40.851184+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37123256692)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1401 ms | 160.7 | 5.27 s | 282 | 621 | $0.000415 |
| DeepSeek | ok | stop | 834 ms | 232.8 | 3.80 s | 282 | 689 | $0.000456 |
| Fireworks | ok | stop | 1211 ms | 62.9 | 14.12 s | 282 | 812 | $0.000598 |
| HAI | ok | stop | 4219 ms | 107.7 | 11.26 s | 293 | 756 | ¥0.1990 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
