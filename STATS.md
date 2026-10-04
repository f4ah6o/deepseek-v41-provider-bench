# Benchmark statistics

Generated: `2026-10-04T23:10:32+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **97**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 97 | 100% | 1381 ms | 2287 ms | 189.8 | 250.5 | 5.25 s | 8.04 s | 703 | $0.000468 |
| DeepSeek | 97 | 100% | 828 ms | 1142 ms | 237.3 | 258.2 | 3.89 s | 4.83 s | 722 | $0.000482 |
| Fireworks | 97 | 100% | 706 ms | 2818 ms | 94.1 | 166.7 | 8.53 s | 14.26 s | 709 | $0.000530 |
| HAI | 97 | 97% | 3479 ms | 24770 ms | 98.0 | 197.7 | 9.98 s | 95.00 s | 569 | ¥0.1542 |

## Latest run

Run `20261004T230951Z-e5be41f2` · `2026-10-04T23:09:51.841817+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37242740641)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1381 ms | 190.8 | 4.50 s | 276 | 595 | $0.000398 |
| DeepSeek | ok | stop | 681 ms | 246.8 | 4.11 s | 276 | 844 | $0.000548 |
| Fireworks | ok | stop | 7819 ms | 67.5 | 16.27 s | 276 | 571 | $0.000438 |
| HAI | ok | stop | 3534 ms | 21.3 | 40.34 s | 287 | 783 | ¥0.2051 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
