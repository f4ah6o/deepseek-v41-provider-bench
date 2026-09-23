# Benchmark statistics

Generated: `2026-09-23T23:42:37+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **44**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 44 | 100% | 1162 ms | 1799 ms | 234.8 | 265.1 | 4.37 s | 7.62 s | 710 | $0.000469 |
| DeepSeek | 44 | 100% | 900 ms | 1132 ms | 237.6 | 259.1 | 3.83 s | 4.65 s | 694 | $0.000476 |
| Fireworks | 44 | 100% | 631 ms | 2299 ms | 98.3 | 180.1 | 7.84 s | 10.68 s | 704 | $0.000526 |
| HAI | 44 | 98% | 3113 ms | 29126 ms | 99.4 | 193.6 | 8.74 s | 103.16 s | 541 | ¥0.1472 |

## Latest run

Run `20260923T234208Z-926c2520` · `2026-09-23T23:42:08.300581+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35934872379)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1475 ms | 155.8 | 7.72 s | 283 | 973 | $0.000626 |
| DeepSeek | ok | stop | 419 ms | 211.5 | 3.93 s | 283 | 742 | $0.000488 |
| Fireworks | ok | stop | 620 ms | 127.8 | 6.46 s | 283 | 746 | $0.000555 |
| HAI | ok | stop | 7352 ms | 28.9 | 28.99 s | 294 | 625 | ¥0.1676 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
