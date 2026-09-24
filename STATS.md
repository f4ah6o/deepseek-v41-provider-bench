# Benchmark statistics

Generated: `2026-09-24T15:06:32+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **47**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 47 | 100% | 1183 ms | 1878 ms | 235.3 | 263.6 | 4.36 s | 7.88 s | 710 | $0.000468 |
| DeepSeek | 47 | 100% | 881 ms | 1126 ms | 237.4 | 258.9 | 3.86 s | 4.64 s | 697 | $0.000477 |
| Fireworks | 47 | 100% | 642 ms | 2592 ms | 97.4 | 178.9 | 7.86 s | 11.07 s | 720 | $0.000536 |
| HAI | 47 | 98% | 3018 ms | 28905 ms | 99.8 | 197.7 | 8.69 s | 101.94 s | 542 | ¥0.1474 |

## Latest run

Run `20260924T150611Z-7eea9e30` · `2026-09-24T15:06:11.856963+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36017642773)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 3631 ms | 151.3 | 7.94 s | 281 | 652 | $0.000433 |
| DeepSeek | ok | stop | 682 ms | 233.6 | 4.10 s | 281 | 798 | $0.000521 |
| Fireworks | ok | stop | 3362 ms | 78.0 | 12.85 s | 281 | 740 | $0.000550 |
| HAI | ok | stop | 14624 ms | 95.8 | 20.56 s | 292 | 565 | ¥0.1531 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
