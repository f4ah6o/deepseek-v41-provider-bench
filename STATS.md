# Benchmark statistics

Generated: `2026-09-19T00:22:26+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **15**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 15 | 100% | 1146 ms | 1614 ms | 236.3 | 266.9 | 4.07 s | 7.08 s | 689 | $0.000455 |
| DeepSeek | 15 | 100% | 946 ms | 1170 ms | 237.9 | 254.1 | 4.05 s | 5.10 s | 697 | $0.000478 |
| Fireworks | 15 | 100% | 688 ms | 1580 ms | 97.4 | 162.6 | 7.62 s | 10.50 s | 720 | $0.000536 |
| HAI | 15 | 93% | 3620 ms | 25285 ms | 95.4 | 132.4 | 18.78 s | 89.81 s | 544 | ¥0.1480 |

## Latest run

Run `20260919T002051Z-bfcccc97` · `2026-09-19T00:20:51.896394+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35409031058)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1251 ms | 171.2 | 5.33 s | 278 | 689 | $0.000455 |
| DeepSeek | ok | stop | 1035 ms | 175.9 | 5.59 s | 278 | 797 | $0.000520 |
| Fireworks | ok | stop | 600 ms | 68.0 | 11.20 s | 278 | 720 | $0.000536 |
| HAI | ok | stop | 7180 ms | 7.3 | 94.54 s | 289 | 636 | ¥0.1700 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
