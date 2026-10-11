# Benchmark statistics

Generated: `2026-10-11T23:43:53+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **126**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 126 | 92% | 1372 ms | 2597 ms | 178.0 | 250.5 | 5.29 s | 8.06 s | 704 | $0.000476 |
| DeepSeek | 126 | 100% | 848 ms | 1179 ms | 236.9 | 256.0 | 3.93 s | 4.93 s | 724 | $0.000484 |
| Fireworks | 126 | 100% | 719 ms | 3050 ms | 97.3 | 181.7 | 7.84 s | 13.64 s | 705 | $0.000527 |
| HAI | 126 | 98% | 3563 ms | 27335 ms | 95.8 | 197.3 | 11.26 s | 95.71 s | 573 | ¥0.1553 |

## Latest run

Run `20261011T234327Z-6645b249` · `2026-10-11T23:43:27.779107+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/38185340871)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | http_error | — | — | — | 0.38 s | — | — | — |
| DeepSeek | ok | stop | 789 ms | 207.4 | 4.88 s | 279 | 848 | $0.000551 |
| Fireworks | ok | stop | 596 ms | 150.0 | 4.62 s | 279 | 604 | $0.000460 |
| HAI | ok | stop | 3661 ms | 24.4 | 25.85 s | 290 | 542 | ¥0.1475 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
