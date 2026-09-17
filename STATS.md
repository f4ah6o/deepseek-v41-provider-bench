# Benchmark statistics

Generated: `2026-09-17T06:08:37+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **5**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 5 | 100% | 1183 ms | 1819 ms | 221.0 | 262.0 | 3.86 s | 7.63 s | 653 | $0.000433 |
| DeepSeek | 5 | 100% | 1102 ms | 1183 ms | 237.9 | 239.8 | 4.27 s | 4.77 s | 722 | $0.000504 |
| Fireworks | 5 | 100% | 889 ms | 2154 ms | 120.0 | 144.8 | 8.53 s | 9.17 s | 721 | $0.000537 |
| HAI | 5 | 100% | 2433 ms | 19817 ms | 99.4 | 145.2 | 8.74 s | 75.58 s | 671 | ¥0.1783 |

## Latest run

Run `20260917T060828Z-8a92d3a8` · `2026-09-17T06:08:28.504055+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35188538967)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1183 ms | 221.0 | 4.45 s | 281 | 710 | $0.000936 |
| DeepSeek | ok | stop | 715 ms | 195.1 | 4.29 s | 281 | 697 | $0.000921 |
| Fireworks | ok | stop | 688 ms | 88.7 | 8.53 s | 281 | 695 | $0.000521 |
| HAI | ok | stop | 2433 ms | 156.4 | 7.33 s | 292 | 761 | ¥0.2002 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
