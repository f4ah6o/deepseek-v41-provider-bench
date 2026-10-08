# Benchmark statistics

Generated: `2026-10-08T01:01:23+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **109**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 109 | 100% | 1375 ms | 2642 ms | 183.3 | 251.0 | 5.31 s | 8.23 s | 705 | $0.000473 |
| DeepSeek | 109 | 100% | 834 ms | 1176 ms | 237.2 | 257.2 | 3.93 s | 4.86 s | 728 | $0.000488 |
| Fireworks | 109 | 100% | 706 ms | 2977 ms | 96.1 | 178.2 | 8.30 s | 13.96 s | 706 | $0.000528 |
| HAI | 109 | 97% | 3548 ms | 28068 ms | 96.2 | 197.6 | 10.29 s | 101.94 s | 566 | ¥0.1532 |

## Latest run

Run `20261008T010031Z-9945bdf1` · `2026-10-08T01:00:31.406794+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37710692021)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 2693 ms | 193.3 | 7.01 s | 282 | 833 | $0.001084 |
| DeepSeek | ok | stop | 1165 ms | 196.6 | 3.33 s | 282 | 423 | $0.000592 |
| Fireworks | ok | stop | 287 ms | 155.7 | 2.74 s | 282 | 381 | $0.000313 |
| HAI | ok | stop | 4483 ms | 15.0 | 51.93 s | 293 | 710 | ¥0.1880 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
