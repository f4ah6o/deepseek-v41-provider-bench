# Benchmark statistics

Generated: `2026-09-20T16:12:41+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **25**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 25 | 100% | 1146 ms | 1485 ms | 237.3 | 266.7 | 4.23 s | 6.28 s | 691 | $0.000456 |
| DeepSeek | 25 | 100% | 940 ms | 1151 ms | 237.9 | 256.8 | 3.93 s | 4.82 s | 697 | $0.000477 |
| Fireworks | 25 | 100% | 689 ms | 2271 ms | 99.1 | 151.6 | 8.13 s | 11.11 s | 702 | $0.000524 |
| HAI | 25 | 96% | 2668 ms | 29052 ms | 99.8 | 231.1 | 7.45 s | 93.45 s | 532 | ¥0.1451 |

## Latest run

Run `20260920T160600Z-5047897e` · `2026-09-20T16:06:00.159172+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35521628721)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1056 ms | 224.1 | 4.99 s | 281 | 880 | $0.000570 |
| DeepSeek | ok | stop | 640 ms | 239.9 | 4.25 s | 281 | 865 | $0.000561 |
| Fireworks | ok | stop | 1289 ms | 103.3 | 10.03 s | 281 | 903 | $0.000658 |
| HAI | ok | stop | 85425 ms | 2.1 | 400.79 s | 292 | 674 | ¥0.1793 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
