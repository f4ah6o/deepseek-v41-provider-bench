# Benchmark statistics

Generated: `2026-09-19T18:01:16+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **19**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 19 | 100% | 1146 ms | 1532 ms | 237.3 | 266.8 | 4.19 s | 6.69 s | 689 | $0.000455 |
| DeepSeek | 19 | 100% | 941 ms | 1165 ms | 237.9 | 258.0 | 3.80 s | 4.96 s | 692 | $0.000475 |
| Fireworks | 19 | 100% | 689 ms | 2717 ms | 97.4 | 156.1 | 8.13 s | 11.42 s | 720 | $0.000536 |
| HAI | 19 | 95% | 2457 ms | 24057 ms | 97.6 | 162.6 | 7.60 s | 88.36 s | 544 | ¥0.1480 |

## Latest run

Run `20260919T180108Z-ca253d3c` · `2026-09-19T18:01:08.759517+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35459844040)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1454 ms | 256.4 | 4.36 s | 279 | 744 | $0.000488 |
| DeepSeek | ok | stop | 941 ms | 237.4 | 4.15 s | 279 | 761 | $0.000498 |
| Fireworks | ok | stop | 1635 ms | 128.2 | 5.32 s | 279 | 472 | $0.000373 |
| HAI | ok | stop | 1886 ms | 103.7 | 6.97 s | 290 | 523 | ¥0.1429 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
