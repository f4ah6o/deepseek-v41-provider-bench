# Benchmark statistics

Generated: `2026-10-10T22:32:15+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **121**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 121 | 96% | 1372 ms | 2597 ms | 178.0 | 250.5 | 5.29 s | 8.06 s | 704 | $0.000476 |
| DeepSeek | 121 | 100% | 847 ms | 1184 ms | 237.3 | 256.0 | 3.93 s | 4.89 s | 722 | $0.000484 |
| Fireworks | 121 | 100% | 720 ms | 3173 ms | 96.9 | 181.9 | 8.06 s | 13.72 s | 706 | $0.000528 |
| HAI | 121 | 98% | 3548 ms | 27855 ms | 96.2 | 197.4 | 11.22 s | 97.06 s | 574 | ¥0.1554 |

## Latest run

Run `20261010T223145Z-9565aec6` · `2026-10-10T22:31:45.449452+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/38091753227)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | http_error | — | — | — | 0.29 s | — | — | — |
| DeepSeek | ok | stop | 1003 ms | 226.6 | 5.53 s | 280 | 1021 | $0.000655 |
| Fireworks | ok | stop | 900 ms | 142.3 | 5.59 s | 280 | 667 | $0.000502 |
| HAI | ok | stop | 3236 ms | 26.3 | 29.93 s | 291 | 700 | ¥0.1855 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
