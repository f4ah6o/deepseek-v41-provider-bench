# Benchmark statistics

Generated: `2026-09-21T00:17:08+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **28**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 28 | 100% | 1141 ms | 1481 ms | 238.5 | 266.7 | 4.21 s | 6.11 s | 700 | $0.000462 |
| DeepSeek | 28 | 100% | 901 ms | 1142 ms | 238.7 | 256.8 | 3.87 s | 4.77 s | 694 | $0.000476 |
| Fireworks | 28 | 100% | 689 ms | 2186 ms | 98.3 | 150.7 | 8.24 s | 11.05 s | 711 | $0.000530 |
| HAI | 28 | 96% | 3447 ms | 28831 ms | 95.8 | 225.2 | 7.62 s | 110.55 s | 523 | ¥0.1429 |

## Latest run

Run `20260921T001641Z-421b77c3` · `2026-09-21T00:16:41.310914+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35547179743)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1099 ms | 238.1 | 4.38 s | 279 | 780 | $0.000510 |
| DeepSeek | ok | stop | 639 ms | 247.5 | 3.34 s | 279 | 667 | $0.000442 |
| Fireworks | ok | stop | 698 ms | 86.3 | 10.16 s | 279 | 817 | $0.000601 |
| HAI | ok | stop | 4085 ms | 20.4 | 26.80 s | 290 | 462 | ¥0.1283 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
