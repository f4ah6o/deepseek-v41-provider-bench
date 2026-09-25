# Benchmark statistics

Generated: `2026-09-25T22:20:37+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **54**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 54 | 100% | 1205 ms | 2652 ms | 231.0 | 260.0 | 4.45 s | 7.80 s | 710 | $0.000472 |
| DeepSeek | 54 | 100% | 889 ms | 1146 ms | 237.1 | 258.4 | 3.86 s | 4.72 s | 696 | $0.000476 |
| Fireworks | 54 | 100% | 631 ms | 2488 ms | 98.8 | 176.2 | 7.74 s | 10.92 s | 713 | $0.000532 |
| HAI | 54 | 98% | 3360 ms | 28390 ms | 100.2 | 213.4 | 9.06 s | 99.09 s | 545 | ¥0.1483 |

## Latest run

Run `20260925T222017Z-53c9fd54` · `2026-09-25T22:20:17.674841+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36196187286)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 3934 ms | 175.4 | 7.69 s | 281 | 658 | $0.000437 |
| DeepSeek | ok | stop | 934 ms | 210.4 | 4.24 s | 281 | 695 | $0.000459 |
| Fireworks | ok | stop | 304 ms | 126.5 | 3.82 s | 281 | 445 | $0.000356 |
| HAI | ok | stop | 3360 ms | 31.1 | 19.13 s | 292 | 488 | ¥0.1346 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
