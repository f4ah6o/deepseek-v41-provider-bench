# Benchmark statistics

Generated: `2026-09-22T22:09:10+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **38**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 38 | 100% | 1128 ms | 1573 ms | 237.7 | 266.6 | 4.25 s | 6.79 s | 710 | $0.000472 |
| DeepSeek | 38 | 100% | 901 ms | 1111 ms | 238.7 | 259.4 | 3.83 s | 4.61 s | 690 | $0.000476 |
| Fireworks | 38 | 100% | 667 ms | 1905 ms | 98.3 | 175.3 | 7.93 s | 10.83 s | 711 | $0.000530 |
| HAI | 38 | 97% | 2854 ms | 33837 ms | 99.4 | 205.6 | 7.62 s | 106.66 s | 520 | ¥0.1422 |

## Latest run

Run `20260922T220905Z-900ec56a` · `2026-09-22T22:09:05.506392+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35790759065)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1233 ms | 218.3 | 4.73 s | 279 | 763 | $0.000500 |
| DeepSeek | ok | stop | 718 ms | 229.2 | 4.53 s | 279 | 874 | $0.000566 |
| Fireworks | ok | stop | 455 ms | 168.6 | 4.45 s | 279 | 673 | $0.000506 |
| HAI | ok | stop | 1753 ms | 144.6 | 4.94 s | 290 | 455 | ¥0.1266 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
