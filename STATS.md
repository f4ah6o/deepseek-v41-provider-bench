# Benchmark statistics

Generated: `2026-09-17T16:59:58+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **7**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 7 | 100% | 1183 ms | 1778 ms | 234.3 | 262.7 | 4.07 s | 7.23 s | 668 | $0.000443 |
| DeepSeek | 7 | 100% | 1010 ms | 1181 ms | 236.9 | 239.7 | 4.14 s | 4.71 s | 697 | $0.000475 |
| Fireworks | 7 | 100% | 688 ms | 2039 ms | 120.0 | 173.8 | 8.13 s | 9.15 s | 702 | $0.000524 |
| HAI | 7 | 100% | 2433 ms | 18157 ms | 99.4 | 140.0 | 7.62 s | 69.73 s | 543 | ¥0.1476 |

## Latest run

Run `20260917T165950Z-9c267fc2` · `2026-09-17T16:59:50.184181+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35249967802)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1146 ms | 251.5 | 4.07 s | 280 | 724 | $0.000476 |
| DeepSeek | ok | stop | 654 ms | 236.9 | 3.25 s | 280 | 614 | $0.000410 |
| Fireworks | ok | stop | 566 ms | 185.3 | 4.02 s | 280 | 639 | $0.000483 |
| HAI | ok | stop | 2854 ms | 95.6 | 7.62 s | 291 | 454 | ¥0.1264 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
