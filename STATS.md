# Benchmark statistics

Generated: `2026-09-25T01:30:29+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **50**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 50 | 100% | 1196 ms | 1867 ms | 233.6 | 262.0 | 4.40 s | 7.84 s | 710 | $0.000469 |
| DeepSeek | 50 | 100% | 875 ms | 1121 ms | 237.1 | 258.7 | 3.87 s | 4.75 s | 702 | $0.000477 |
| Fireworks | 50 | 100% | 631 ms | 2547 ms | 98.8 | 177.8 | 7.84 s | 11.00 s | 713 | $0.000532 |
| HAI | 50 | 98% | 3113 ms | 28684 ms | 100.2 | 221.3 | 8.74 s | 100.72 s | 545 | ¥0.1483 |

## Latest run

Run `20260925T013020Z-0fa1a9aa` · `2026-09-25T01:30:20.853393+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36082283210)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1414 ms | 144.9 | 7.17 s | 281 | 833 | $0.001084 |
| DeepSeek | ok | stop | 964 ms | 225.4 | 4.81 s | 281 | 867 | $0.001125 |
| Fireworks | ok | stop | 604 ms | 105.7 | 6.47 s | 281 | 620 | $0.000471 |
| HAI | ok | stop | 1662 ms | 102.3 | 8.20 s | 292 | 665 | ¥0.1771 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
