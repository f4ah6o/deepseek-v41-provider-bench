# Benchmark statistics

Generated: `2026-09-23T05:59:36+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **40**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 40 | 100% | 1133 ms | 1829 ms | 236.8 | 266.6 | 4.27 s | 7.10 s | 712 | $0.000472 |
| DeepSeek | 40 | 100% | 908 ms | 1138 ms | 238.7 | 259.3 | 3.83 s | 4.68 s | 690 | $0.000476 |
| Fireworks | 40 | 100% | 647 ms | 1849 ms | 99.7 | 181.5 | 7.74 s | 10.79 s | 704 | $0.000526 |
| HAI | 40 | 98% | 2923 ms | 31555 ms | 99.4 | 201.6 | 8.64 s | 105.32 s | 523 | ¥0.1429 |

## Latest run

Run `20260923T055830Z-14b1b171` · `2026-09-23T05:58:30.409261+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35824631007)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1826 ms | 136.8 | 7.03 s | 280 | 712 | $0.000469 |
| DeepSeek | ok | stop | 1137 ms | 207.5 | 4.67 s | 280 | 733 | $0.000482 |
| Fireworks | ok | stop | 512 ms | 158.3 | 5.00 s | 280 | 706 | $0.000528 |
| HAI | ok | stop | 3907 ms | 10.0 | 66.08 s | 291 | 619 | ¥0.1660 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
