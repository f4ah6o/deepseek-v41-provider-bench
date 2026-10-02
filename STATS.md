# Benchmark statistics

Generated: `2026-10-02T02:15:50+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **83**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 83 | 100% | 1335 ms | 2522 ms | 195.7 | 251.3 | 5.23 s | 8.38 s | 710 | $0.000469 |
| DeepSeek | 83 | 100% | 845 ms | 1160 ms | 237.0 | 256.0 | 3.87 s | 4.72 s | 714 | $0.000481 |
| Fireworks | 83 | 100% | 688 ms | 2470 ms | 96.5 | 168.4 | 8.27 s | 12.84 s | 721 | $0.000537 |
| HAI | 83 | 98% | 3322 ms | 27801 ms | 100.2 | 197.7 | 9.78 s | 95.84 s | 573 | ¥0.1553 |

## Latest run

Run `20261002T021541Z-f8863a3a` · `2026-10-02T02:15:41.550915+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36954790267)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1530 ms | 173.3 | 5.94 s | 277 | 764 | $0.001000 |
| DeepSeek | ok | stop | 703 ms | 231.0 | 4.25 s | 277 | 819 | $0.001066 |
| Fireworks | ok | stop | 953 ms | 91.2 | 8.95 s | 277 | 729 | $0.000542 |
| HAI | ok | stop | 2028 ms | 112.7 | 7.32 s | 288 | 591 | ¥0.1591 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
