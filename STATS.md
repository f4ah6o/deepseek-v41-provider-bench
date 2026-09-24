# Benchmark statistics

Generated: `2026-09-24T10:01:04+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **46**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 46 | 100% | 1180 ms | 1781 ms | 235.7 | 264.1 | 4.32 s | 7.55 s | 710 | $0.000468 |
| DeepSeek | 46 | 100% | 889 ms | 1128 ms | 237.6 | 258.9 | 3.83 s | 4.64 s | 694 | $0.000476 |
| Fireworks | 46 | 100% | 631 ms | 2243 ms | 98.3 | 179.3 | 7.84 s | 10.62 s | 713 | $0.000532 |
| HAI | 46 | 98% | 2923 ms | 28978 ms | 100.2 | 197.7 | 8.64 s | 102.35 s | 541 | ¥0.1472 |

## Latest run

Run `20260924T100055Z-3318f87e` · `2026-09-24T10:00:55.116778+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35984706778)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1242 ms | 237.9 | 4.12 s | 281 | 683 | $0.000452 |
| DeepSeek | ok | stop | 751 ms | 237.3 | 4.07 s | 281 | 786 | $0.000514 |
| Fireworks | ok | stop | 614 ms | 91.0 | 9.47 s | 281 | 806 | $0.000594 |
| HAI | ok | stop | 1899 ms | 197.4 | 5.58 s | 292 | 713 | ¥0.1886 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
