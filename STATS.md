# Benchmark statistics

Generated: `2026-10-05T09:04:40+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **99**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 99 | 100% | 1381 ms | 2252 ms | 185.3 | 250.4 | 5.27 s | 7.99 s | 705 | $0.000469 |
| DeepSeek | 99 | 100% | 828 ms | 1162 ms | 237.3 | 258.0 | 3.90 s | 4.82 s | 725 | $0.000484 |
| Fireworks | 99 | 100% | 718 ms | 3192 ms | 93.5 | 166.5 | 8.54 s | 14.19 s | 709 | $0.000530 |
| HAI | 99 | 97% | 3479 ms | 24303 ms | 98.0 | 197.7 | 9.98 s | 94.87 s | 560 | ¥0.1520 |

## Latest run

Run `20261005T090413Z-e54498ba` · `2026-10-05T09:04:13.558200+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37287591045)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1492 ms | 177.7 | 5.86 s | 278 | 776 | $0.001015 |
| DeepSeek | ok | stop | 1184 ms | 243.2 | 4.25 s | 278 | 745 | $0.000977 |
| Fireworks | ok | stop | 3173 ms | 62.5 | 11.29 s | 278 | 503 | $0.000393 |
| HAI | ok | stop | 4342 ms | 25.1 | 26.21 s | 289 | 548 | ¥0.1489 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
