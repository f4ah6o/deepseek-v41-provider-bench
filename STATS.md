# Benchmark statistics

Generated: `2026-09-28T22:00:48+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **69**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 69 | 100% | 1284 ms | 2035 ms | 222.4 | 254.4 | 4.73 s | 7.85 s | 705 | $0.000468 |
| DeepSeek | 69 | 100% | 881 ms | 1152 ms | 237.0 | 257.0 | 3.86 s | 4.71 s | 722 | $0.000480 |
| Fireworks | 69 | 100% | 656 ms | 2441 ms | 96.9 | 171.5 | 7.81 s | 12.83 s | 709 | $0.000530 |
| HAI | 69 | 99% | 3404 ms | 26169 ms | 100.2 | 223.2 | 9.12 s | 95.39 s | 552 | ¥0.1498 |

## Latest run

Run `20260928T220034Z-2da1ce0b` · `2026-09-28T22:00:34.388168+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36489744235)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1464 ms | 160.9 | 4.23 s | 282 | 445 | $0.000309 |
| DeepSeek | ok | stop | 792 ms | 225.6 | 2.27 s | 282 | 331 | $0.000241 |
| Fireworks | ok | stop | 2479 ms | 69.2 | 12.79 s | 282 | 714 | $0.000533 |
| HAI | ok | stop | 3602 ms | 33.7 | 14.17 s | 293 | 355 | ¥0.1028 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
