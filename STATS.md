# Benchmark statistics

Generated: `2026-10-11T20:16:58+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **125**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 125 | 93% | 1372 ms | 2597 ms | 178.0 | 250.5 | 5.29 s | 8.06 s | 704 | $0.000476 |
| DeepSeek | 125 | 100% | 849 ms | 1180 ms | 237.0 | 256.0 | 3.93 s | 4.93 s | 722 | $0.000484 |
| Fireworks | 125 | 100% | 720 ms | 3075 ms | 97.2 | 181.7 | 7.86 s | 13.65 s | 705 | $0.000527 |
| HAI | 125 | 98% | 3548 ms | 27568 ms | 95.8 | 197.4 | 11.22 s | 95.77 s | 574 | ¥0.1554 |

## Latest run

Run `20261011T201635Z-0e30eb20` · `2026-10-11T20:16:35.432058+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/38171503651)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | http_error | — | — | — | 0.48 s | — | — | — |
| DeepSeek | ok | stop | 828 ms | 220.7 | 3.86 s | 282 | 668 | $0.000443 |
| Fireworks | ok | stop | 760 ms | 139.9 | 6.15 s | 282 | 754 | $0.000560 |
| HAI | ok | stop | 3587 ms | 29.6 | 22.72 s | 293 | 565 | ¥0.1532 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
