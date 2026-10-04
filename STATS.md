# Benchmark statistics

Generated: `2026-10-04T19:39:16+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **96**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 96 | 100% | 1388 ms | 2304 ms | 187.6 | 250.5 | 5.26 s | 8.06 s | 704 | $0.000469 |
| DeepSeek | 96 | 100% | 830 ms | 1143 ms | 237.1 | 258.3 | 3.88 s | 4.83 s | 720 | $0.000481 |
| Fireworks | 96 | 100% | 704 ms | 2646 ms | 94.7 | 166.8 | 8.44 s | 13.82 s | 712 | $0.000532 |
| HAI | 96 | 97% | 3447 ms | 25003 ms | 99.4 | 197.7 | 9.95 s | 95.06 s | 565 | ¥0.1531 |

## Latest run

Run `20261004T193842Z-8c39e167` · `2026-10-04T19:38:42.789217+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37229052912)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1461 ms | 167.0 | 7.18 s | 276 | 954 | $0.000614 |
| DeepSeek | ok | stop | 495 ms | 243.0 | 3.82 s | 276 | 807 | $0.000526 |
| Fireworks | ok | stop | 751 ms | 51.4 | 13.72 s | 276 | 667 | $0.000501 |
| HAI | ok | stop | 4782 ms | 25.0 | 32.98 s | 287 | 705 | ¥0.1864 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
