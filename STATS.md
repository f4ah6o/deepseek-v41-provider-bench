# Benchmark statistics

Generated: `2026-10-11T08:50:43+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **123**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 123 | 94% | 1372 ms | 2597 ms | 178.0 | 250.5 | 5.29 s | 8.06 s | 704 | $0.000476 |
| DeepSeek | 123 | 100% | 849 ms | 1182 ms | 237.2 | 256.0 | 3.93 s | 4.93 s | 725 | $0.000485 |
| Fireworks | 123 | 100% | 718 ms | 3124 ms | 96.9 | 181.8 | 8.01 s | 13.69 s | 705 | $0.000527 |
| HAI | 123 | 98% | 3523 ms | 27819 ms | 96.2 | 197.4 | 10.79 s | 96.24 s | 576 | ¥0.1558 |

## Latest run

Run `20261011T085034Z-241ed51e` · `2026-10-11T08:50:34.236829+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/38126220864)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | http_error | — | — | — | 0.36 s | — | — | — |
| DeepSeek | ok | stop | 1031 ms | 228.9 | 4.36 s | 278 | 762 | $0.000499 |
| Fireworks | ok | stop | 426 ms | 165.3 | 4.31 s | 278 | 641 | $0.000484 |
| HAI | ok | stop | 2262 ms | 102.7 | 8.54 s | 289 | 640 | ¥0.1709 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
