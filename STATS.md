# Benchmark statistics

Generated: `2026-09-28T06:54:17+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **67**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 67 | 100% | 1274 ms | 2058 ms | 223.0 | 254.9 | 4.73 s | 7.88 s | 710 | $0.000468 |
| DeepSeek | 67 | 100% | 881 ms | 1155 ms | 237.0 | 257.3 | 3.86 s | 4.71 s | 722 | $0.000481 |
| Fireworks | 67 | 100% | 652 ms | 2336 ms | 96.9 | 172.0 | 7.67 s | 12.52 s | 706 | $0.000528 |
| HAI | 67 | 99% | 3237 ms | 26635 ms | 100.9 | 227.2 | 9.07 s | 95.51 s | 552 | ¥0.1498 |

## Latest run

Run `20260928T065405Z-07ed6e33` · `2026-09-28T06:54:05.804487+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36388755481)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1489 ms | 120.8 | 9.02 s | 280 | 909 | $0.001175 |
| DeepSeek | ok | stop | 1000 ms | 237.0 | 4.50 s | 280 | 829 | $0.001079 |
| Fireworks | ok | stop | 1304 ms | 77.2 | 11.74 s | 280 | 806 | $0.000594 |
| HAI | ok | stop | 2245 ms | 160.2 | 6.16 s | 291 | 624 | ¥0.1672 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
