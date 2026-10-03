# Benchmark statistics

Generated: `2026-10-03T17:16:55+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **90**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 90 | 100% | 1360 ms | 2367 ms | 185.1 | 250.9 | 5.24 s | 8.21 s | 708 | $0.000472 |
| DeepSeek | 90 | 100% | 840 ms | 1151 ms | 237.1 | 257.1 | 3.88 s | 4.81 s | 716 | $0.000480 |
| Fireworks | 90 | 100% | 689 ms | 2590 ms | 96.2 | 167.5 | 8.29 s | 13.20 s | 717 | $0.000535 |
| HAI | 90 | 97% | 3324 ms | 26402 ms | 100.2 | 197.7 | 9.78 s | 95.45 s | 573 | ¥0.1553 |

## Latest run

Run `20261003T171642Z-50602151` · `2026-10-03T17:16:42.502861+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37139907883)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1560 ms | 182.1 | 5.22 s | 277 | 666 | $0.000441 |
| DeepSeek | ok | stop | 755 ms | 263.5 | 3.17 s | 277 | 635 | $0.000423 |
| Fireworks | ok | stop | 1432 ms | 59.0 | 13.01 s | 277 | 683 | $0.000512 |
| HAI | ok | stop | 2026 ms | 133.6 | 6.38 s | 288 | 582 | ¥0.1570 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
