# Benchmark statistics

Generated: `2026-09-19T10:58:51+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **17**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 17 | 100% | 1137 ms | 1573 ms | 237.3 | 266.8 | 4.07 s | 6.88 s | 689 | $0.000455 |
| DeepSeek | 17 | 100% | 946 ms | 1168 ms | 237.9 | 253.6 | 3.80 s | 5.03 s | 692 | $0.000475 |
| Fireworks | 17 | 100% | 688 ms | 3050 ms | 97.4 | 159.4 | 8.13 s | 11.64 s | 721 | $0.000537 |
| HAI | 17 | 94% | 2644 ms | 24671 ms | 95.7 | 166.7 | 8.18 s | 89.08 s | 581 | ¥0.1568 |

## Latest run

Run `20260919T105841Z-090db3ac` · `2026-09-19T10:58:41.071536+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35438832031)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 895 ms | 246.1 | 3.60 s | 280 | 664 | $0.000440 |
| DeepSeek | ok | stop | 699 ms | 251.3 | 3.24 s | 280 | 639 | $0.000425 |
| Fireworks | ok | stop | 1821 ms | 96.3 | 9.81 s | 280 | 769 | $0.000569 |
| HAI | ok | stop | 1469 ms | 116.3 | 7.58 s | 291 | 704 | ¥0.1864 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
