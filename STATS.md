# Benchmark statistics

Generated: `2026-10-11T15:41:03+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **124**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 124 | 94% | 1372 ms | 2597 ms | 178.0 | 250.5 | 5.29 s | 8.06 s | 704 | $0.000476 |
| DeepSeek | 124 | 100% | 855 ms | 1181 ms | 237.1 | 256.0 | 3.93 s | 4.93 s | 724 | $0.000484 |
| Fireworks | 124 | 100% | 719 ms | 3099 ms | 97.0 | 181.8 | 7.93 s | 13.67 s | 705 | $0.000527 |
| HAI | 124 | 98% | 3534 ms | 27801 ms | 95.8 | 197.4 | 11.18 s | 95.84 s | 576 | ¥0.1555 |

## Latest run

Run `20261011T154041Z-3c44ad15` · `2026-10-11T15:40:41.688987+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/38152262063)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | http_error | — | — | — | 0.68 s | — | — | — |
| DeepSeek | ok | stop | 908 ms | 190.4 | 3.77 s | 277 | 545 | $0.000369 |
| Fireworks | ok | stop | 1320 ms | 128.9 | 6.36 s | 277 | 646 | $0.000487 |
| HAI | ok | stop | 3657 ms | 23.0 | 21.32 s | 288 | 403 | ¥0.1140 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
