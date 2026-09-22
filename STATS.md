# Benchmark statistics

Generated: `2026-09-22T04:57:41+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **34**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 34 | 100% | 1128 ms | 1634 ms | 237.7 | 266.6 | 4.21 s | 7.17 s | 710 | $0.000468 |
| DeepSeek | 34 | 100% | 908 ms | 1123 ms | 238.7 | 258.4 | 3.87 s | 4.67 s | 694 | $0.000476 |
| Fireworks | 34 | 100% | 685 ms | 2018 ms | 97.3 | 157.5 | 8.24 s | 10.92 s | 720 | $0.000537 |
| HAI | 34 | 97% | 3447 ms | 38402 ms | 99.4 | 213.4 | 7.62 s | 109.35 s | 523 | ¥0.1429 |

## Latest run

Run `20260922T045605Z-b92a3056` · `2026-09-22T04:56:05.684887+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35688745325)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1063 ms | 232.9 | 4.12 s | 278 | 710 | $0.000468 |
| DeepSeek | ok | stop | 910 ms | 233.3 | 2.92 s | 278 | 469 | $0.000323 |
| Fireworks | ok | stop | 373 ms | 166.3 | 6.50 s | 278 | 1019 | $0.000734 |
| HAI | ok | stop | 4573 ms | 5.4 | 95.84 s | 289 | 491 | ¥0.1352 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
