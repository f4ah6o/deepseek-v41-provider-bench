# Benchmark statistics

Generated: `2026-09-25T07:48:40+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **51**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 51 | 100% | 1199 ms | 1869 ms | 232.9 | 261.5 | 4.41 s | 7.83 s | 710 | $0.000469 |
| DeepSeek | 51 | 100% | 881 ms | 1120 ms | 236.9 | 258.6 | 3.86 s | 4.74 s | 700 | $0.000478 |
| Fireworks | 51 | 100% | 642 ms | 2532 ms | 98.4 | 177.4 | 7.86 s | 10.98 s | 720 | $0.000536 |
| HAI | 51 | 98% | 3054 ms | 28611 ms | 100.2 | 219.3 | 8.80 s | 100.31 s | 546 | ¥0.1485 |

## Latest run

Run `20260925T074829Z-d3bae520` · `2026-09-25T07:48:29.239234+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36109517245)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1837 ms | 135.1 | 6.39 s | 276 | 615 | $0.000821 |
| DeepSeek | ok | stop | 881 ms | 191.9 | 3.58 s | 276 | 517 | $0.000703 |
| Fireworks | ok | stop | 706 ms | 75.2 | 10.52 s | 276 | 738 | $0.000548 |
| HAI | ok | stop | 2995 ms | 106.8 | 9.78 s | 287 | 721 | ¥0.1903 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
