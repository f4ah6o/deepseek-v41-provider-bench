# Benchmark statistics

Generated: `2026-09-28T15:28:35+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **68**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 68 | 100% | 1279 ms | 2047 ms | 222.7 | 254.7 | 4.75 s | 7.86 s | 708 | $0.000468 |
| DeepSeek | 68 | 100% | 888 ms | 1153 ms | 237.1 | 257.1 | 3.87 s | 4.71 s | 724 | $0.000480 |
| Fireworks | 68 | 100% | 654 ms | 2328 ms | 96.9 | 171.8 | 7.74 s | 12.46 s | 708 | $0.000529 |
| HAI | 68 | 99% | 3360 ms | 26402 ms | 100.2 | 225.2 | 9.09 s | 95.45 s | 556 | ¥0.1509 |

## Latest run

Run `20260928T152743Z-d9f21572` · `2026-09-28T15:27:43.577572+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36443733087)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1509 ms | 136.7 | 6.67 s | 281 | 705 | $0.000465 |
| DeepSeek | ok | stop | 1044 ms | 252.9 | 3.94 s | 281 | 728 | $0.000479 |
| Fireworks | ok | stop | 827 ms | 77.0 | 10.25 s | 281 | 726 | $0.000541 |
| HAI | ok | stop | 6741 ms | 16.4 | 51.64 s | 292 | 737 | ¥0.1944 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
