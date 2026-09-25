# Benchmark statistics

Generated: `2026-09-25T18:36:52+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **53**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 53 | 100% | 1204 ms | 1990 ms | 232.5 | 260.5 | 4.45 s | 7.81 s | 711 | $0.000476 |
| DeepSeek | 53 | 100% | 881 ms | 1147 ms | 237.3 | 258.5 | 3.86 s | 4.73 s | 697 | $0.000477 |
| Fireworks | 53 | 100% | 642 ms | 2503 ms | 98.4 | 176.6 | 7.81 s | 10.94 s | 720 | $0.000536 |
| HAI | 53 | 98% | 3280 ms | 28463 ms | 100.9 | 215.4 | 8.96 s | 99.50 s | 546 | ¥0.1485 |

## Latest run

Run `20260925T183641Z-ba43e749` · `2026-09-25T18:36:41.692223+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36174497752)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 2125 ms | 150.9 | 7.01 s | 281 | 737 | $0.000484 |
| DeepSeek | ok | stop | 1162 ms | 254.5 | 3.86 s | 281 | 686 | $0.000454 |
| Fireworks | ok | stop | 523 ms | 125.3 | 7.07 s | 281 | 820 | $0.000603 |
| HAI | ok | stop | 7365 ms | 156.1 | 10.17 s | 292 | 381 | ¥0.1090 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
