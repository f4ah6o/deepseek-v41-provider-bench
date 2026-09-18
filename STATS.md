# Benchmark statistics

Generated: `2026-09-18T09:47:25+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **11**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 11 | 100% | 1125 ms | 1696 ms | 236.3 | 267.0 | 4.07 s | 6.48 s | 668 | $0.000443 |
| DeepSeek | 11 | 100% | 946 ms | 1176 ms | 237.9 | 254.9 | 4.05 s | 4.72 s | 697 | $0.000478 |
| Fireworks | 11 | 100% | 688 ms | 1810 ms | 97.2 | 166.1 | 8.13 s | 10.03 s | 702 | $0.000524 |
| HAI | 11 | 100% | 2854 ms | 19851 ms | 95.8 | 137.9 | 8.74 s | 77.07 s | 543 | ¥0.1476 |

## Latest run

Run `20260918T094617Z-db17bb28` · `2026-09-18T09:46:17.885297+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35331251585)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 890 ms | 227.3 | 4.41 s | 280 | 791 | $0.001033 |
| DeepSeek | ok | stop | 896 ms | 251.9 | 3.59 s | 280 | 674 | $0.000893 |
| Fireworks | ok | stop | 431 ms | 96.7 | 9.86 s | 280 | 911 | $0.000663 |
| HAI | ok | stop | 16565 ms | 15.4 | 66.88 s | 291 | 777 | ¥0.2039 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
