# Benchmark statistics

Generated: `2026-10-06T07:34:39+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **102**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 102 | 100% | 1378 ms | 2213 ms | 184.1 | 250.1 | 5.29 s | 7.93 s | 708 | $0.000471 |
| DeepSeek | 102 | 100% | 826 ms | 1161 ms | 237.3 | 257.8 | 3.92 s | 4.81 s | 726 | $0.000484 |
| Fireworks | 102 | 100% | 719 ms | 3149 ms | 93.8 | 168.5 | 8.54 s | 14.10 s | 708 | $0.000529 |
| HAI | 102 | 97% | 3447 ms | 23603 ms | 99.4 | 197.7 | 9.95 s | 94.67 s | 556 | ¥0.1509 |

## Latest run

Run `20261006T073432Z-beb1ee92` · `2026-10-06T07:34:32.642809+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37430497552)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1515 ms | 159.4 | 6.85 s | 278 | 849 | $0.001102 |
| DeepSeek | ok | stop | 860 ms | 235.4 | 3.99 s | 278 | 737 | $0.000968 |
| Fireworks | ok | stop | 834 ms | 145.9 | 4.43 s | 278 | 524 | $0.000407 |
| HAI | ok | stop | 1915 ms | 143.6 | 5.14 s | 289 | 459 | ¥0.1275 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
