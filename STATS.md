# Benchmark statistics

Generated: `2026-10-05T02:01:11+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **98**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 98 | 100% | 1378 ms | 2270 ms | 187.6 | 250.4 | 5.26 s | 8.01 s | 704 | $0.000469 |
| DeepSeek | 98 | 100% | 826 ms | 1141 ms | 237.1 | 258.1 | 3.90 s | 4.83 s | 724 | $0.000483 |
| Fireworks | 98 | 100% | 712 ms | 2784 ms | 93.8 | 166.6 | 8.54 s | 14.23 s | 709 | $0.000530 |
| HAI | 98 | 97% | 3447 ms | 24536 ms | 99.4 | 197.7 | 9.95 s | 94.93 s | 565 | ¥0.1531 |

## Latest run

Run `20261005T020059Z-204df807` · `2026-10-05T02:00:59.509573+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37253676150)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1374 ms | 173.5 | 6.86 s | 278 | 951 | $0.001225 |
| DeepSeek | ok | stop | 532 ms | 232.3 | 4.41 s | 278 | 900 | $0.001163 |
| Fireworks | ok | stop | 914 ms | 64.9 | 11.57 s | 278 | 691 | $0.000517 |
| HAI | ok | stop | 2130 ms | 145.0 | 5.58 s | 289 | 493 | ¥0.1357 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
