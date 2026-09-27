# Benchmark statistics

Generated: `2026-09-27T08:10:06+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **62**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 62 | 100% | 1238 ms | 2114 ms | 226.3 | 256.2 | 4.54 s | 7.72 s | 706 | $0.000468 |
| DeepSeek | 62 | 100% | 874 ms | 1161 ms | 237.3 | 257.8 | 3.84 s | 4.72 s | 702 | $0.000477 |
| Fireworks | 62 | 100% | 647 ms | 2376 ms | 97.3 | 173.2 | 7.74 s | 12.76 s | 708 | $0.000529 |
| HAI | 62 | 98% | 3447 ms | 27801 ms | 100.2 | 237.0 | 9.78 s | 95.84 s | 547 | ¥0.1487 |

## Latest run

Run `20260927T080955Z-99f9af6a` · `2026-09-27T08:09:55.178787+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36305325855)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1797 ms | 152.5 | 5.98 s | 279 | 637 | $0.000424 |
| DeepSeek | ok | stop | 828 ms | 248.2 | 4.27 s | 279 | 855 | $0.000555 |
| Fireworks | ok | stop | 2226 ms | 91.2 | 11.20 s | 279 | 819 | $0.000602 |
| HAI | ok | stop | 4599 ms | 91.7 | 10.01 s | 290 | 494 | ¥0.1360 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
