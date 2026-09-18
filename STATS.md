# Benchmark statistics

Generated: `2026-09-18T18:30:06+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **13**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 13 | 100% | 1146 ms | 1655 ms | 236.3 | 267.0 | 4.07 s | 7.27 s | 668 | $0.000443 |
| DeepSeek | 13 | 100% | 946 ms | 1173 ms | 237.9 | 254.7 | 4.05 s | 4.69 s | 697 | $0.000478 |
| Fireworks | 13 | 100% | 688 ms | 1695 ms | 97.4 | 165.8 | 7.62 s | 9.99 s | 702 | $0.000524 |
| HAI | 13 | 92% | 3620 ms | 25898 ms | 95.7 | 136.1 | 18.78 s | 76.05 s | 544 | ¥0.1480 |

## Latest run

Run `20260918T182906Z-b781c5f6` · `2026-09-18T18:29:06.121971+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35380422836)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1207 ms | 266.7 | 3.59 s | 281 | 614 | $0.000411 |
| DeepSeek | ok | stop | 1065 ms | 252.5 | 4.09 s | 281 | 761 | $0.000499 |
| Fireworks | ok | stop | 1059 ms | 119.8 | 6.79 s | 281 | 668 | $0.000503 |
| HAI | ok | stop | 29273 ms | 17.9 | 59.79 s | 292 | 545 | ¥0.1483 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
