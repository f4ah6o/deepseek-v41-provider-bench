# Benchmark statistics

Generated: `2026-09-27T22:11:05+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **65**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 65 | 100% | 1251 ms | 2080 ms | 224.1 | 255.4 | 4.57 s | 7.71 s | 703 | $0.000468 |
| DeepSeek | 65 | 100% | 881 ms | 1157 ms | 237.3 | 257.5 | 3.86 s | 4.71 s | 714 | $0.000480 |
| Fireworks | 65 | 100% | 642 ms | 2352 ms | 97.2 | 172.5 | 7.67 s | 12.52 s | 706 | $0.000528 |
| HAI | 65 | 98% | 3404 ms | 27102 ms | 100.9 | 231.1 | 9.11 s | 95.64 s | 546 | ¥0.1485 |

## Latest run

Run `20260927T221058Z-0df1707d` · `2026-09-27T22:10:58.324732+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36354371623)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1807 ms | 164.2 | 6.23 s | 279 | 725 | $0.000477 |
| DeepSeek | ok | stop | 818 ms | 235.9 | 4.13 s | 279 | 777 | $0.000508 |
| Fireworks | ok | stop | 546 ms | 96.7 | 6.48 s | 279 | 574 | $0.000440 |
| HAI | ok | stop | 1782 ms | 102.2 | 5.62 s | 290 | 389 | ¥0.1108 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
