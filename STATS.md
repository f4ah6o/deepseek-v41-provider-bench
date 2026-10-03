# Benchmark statistics

Generated: `2026-10-03T00:30:37+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **87**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 87 | 100% | 1337 ms | 2433 ms | 189.8 | 251.1 | 5.23 s | 8.28 s | 710 | $0.000476 |
| DeepSeek | 87 | 100% | 845 ms | 1155 ms | 237.0 | 255.9 | 3.89 s | 4.79 s | 719 | $0.000481 |
| Fireworks | 87 | 100% | 688 ms | 2621 ms | 96.5 | 167.9 | 8.13 s | 12.96 s | 720 | $0.000536 |
| HAI | 87 | 97% | 3341 ms | 27102 ms | 100.2 | 197.7 | 9.81 s | 95.64 s | 569 | ¥0.1542 |

## Latest run

Run `20261003T002959Z-bd23e7dd` · `2026-10-03T00:29:59.847802+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37082302073)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1375 ms | 176.6 | 5.62 s | 280 | 750 | $0.000492 |
| DeepSeek | ok | stop | 786 ms | 233.4 | 3.41 s | 280 | 613 | $0.000410 |
| Fireworks | ok | stop | 982 ms | 74.8 | 6.95 s | 280 | 446 | $0.000356 |
| HAI | ok | stop | 8469 ms | 27.2 | 37.35 s | 291 | 780 | ¥0.2047 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
