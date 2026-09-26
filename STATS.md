# Benchmark statistics

Generated: `2026-09-26T19:52:22+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **59**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 59 | 100% | 1213 ms | 2276 ms | 229.2 | 257.5 | 4.52 s | 7.74 s | 710 | $0.000469 |
| DeepSeek | 59 | 100% | 881 ms | 1162 ms | 236.9 | 258.0 | 3.86 s | 4.73 s | 697 | $0.000477 |
| Fireworks | 59 | 100% | 642 ms | 2413 ms | 97.4 | 174.3 | 7.81 s | 12.86 s | 709 | $0.000530 |
| HAI | 59 | 98% | 3479 ms | 28022 ms | 100.2 | 238.3 | 9.81 s | 97.06 s | 552 | ¥0.1498 |

## Latest run

Run `20260926T195153Z-ad9e3bdc` · `2026-09-26T19:51:53.751852+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36267504370)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1739 ms | 174.3 | 5.62 s | 284 | 675 | $0.000448 |
| DeepSeek | ok | stop | 1001 ms | 238.1 | 4.24 s | 284 | 770 | $0.000505 |
| Fireworks | ok | stop | 1938 ms | 58.7 | 13.01 s | 284 | 650 | $0.000491 |
| HAI | ok | stop | 3511 ms | 29.3 | 28.79 s | 295 | 738 | ¥0.1948 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
