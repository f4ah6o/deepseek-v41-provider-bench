# Benchmark statistics

Generated: `2026-09-16T15:24:05+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **1**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 1 | 100% | 1491 ms | 1491 ms | 216.5 | 216.5 | 3.86 s | 3.86 s | 500 | $0.000342 |
| DeepSeek | 1 | 100% | 1010 ms | 1010 ms | 239.4 | 239.4 | 4.27 s | 4.27 s | 780 | $0.000510 |
| Fireworks | 1 | 100% | 889 ms | 889 ms | 136.8 | 136.8 | 6.02 s | 6.02 s | 702 | $0.000524 |
| HAI | 1 | 100% | 23137 ms | 23137 ms | 95.8 | 95.8 | 28.82 s | 28.82 s | 543 | ¥0.1476 |

## Latest run

Run `20260916T151809Z-61253d1a` · `2026-09-16T15:18:09.148298+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35114368450)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1491 ms | 216.5 | 3.86 s | 277 | 500 | $0.000342 |
| DeepSeek | ok | stop | 1010 ms | 239.4 | 4.27 s | 277 | 780 | $0.000510 |
| Fireworks | ok | stop | 889 ms | 136.8 | 6.02 s | 277 | 702 | $0.000524 |
| HAI | ok | stop | 23137 ms | 95.8 | 28.82 s | 288 | 543 | ¥0.1476 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
