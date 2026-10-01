# Benchmark statistics

Generated: `2026-10-01T18:54:43+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **81**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 81 | 100% | 1335 ms | 2566 ms | 206.2 | 251.5 | 5.13 s | 8.42 s | 705 | $0.000468 |
| DeepSeek | 81 | 100% | 868 ms | 1162 ms | 237.0 | 256.0 | 3.87 s | 4.72 s | 714 | $0.000481 |
| Fireworks | 81 | 100% | 682 ms | 2479 ms | 96.5 | 168.6 | 8.13 s | 12.85 s | 720 | $0.000536 |
| HAI | 81 | 98% | 3360 ms | 27837 ms | 100.1 | 201.6 | 9.78 s | 96.65 s | 565 | ¥0.1531 |

## Latest run

Run `20261001T185426Z-ff019cb2` · `2026-10-01T18:54:26.205381+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36910305560)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 8014 ms | 66.3 | 17.48 s | 280 | 625 | $0.000417 |
| DeepSeek | ok | stop | 2856 ms | 242.0 | 5.55 s | 280 | 652 | $0.000433 |
| Fireworks | ok | stop | 1879 ms | 92.8 | 9.78 s | 280 | 733 | $0.000545 |
| HAI | ok | stop | 1890 ms | 106.3 | 9.29 s | 291 | 782 | ¥0.2051 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
