# Benchmark statistics

Generated: `2026-10-05T18:28:04+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **100**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 100 | 100% | 1378 ms | 2235 ms | 185.1 | 250.3 | 5.27 s | 7.97 s | 704 | $0.000469 |
| DeepSeek | 100 | 100% | 826 ms | 1162 ms | 237.3 | 258.0 | 3.92 s | 4.82 s | 726 | $0.000484 |
| Fireworks | 100 | 100% | 719 ms | 3183 ms | 93.1 | 166.4 | 8.61 s | 14.15 s | 709 | $0.000530 |
| HAI | 100 | 97% | 3447 ms | 24070 ms | 99.4 | 197.7 | 9.95 s | 94.80 s | 556 | ¥0.1509 |

## Latest run

Run `20261005T182754Z-057f93fc` · `2026-10-05T18:27:54.751436+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37356111679)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1329 ms | 174.0 | 5.27 s | 282 | 686 | $0.000454 |
| DeepSeek | ok | stop | 797 ms | 244.6 | 3.98 s | 282 | 778 | $0.000509 |
| Fireworks | ok | stop | 1014 ms | 88.7 | 9.44 s | 282 | 744 | $0.000553 |
| HAI | ok | stop | 1786 ms | 100.2 | 6.81 s | 293 | 500 | ¥0.1376 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
