# Benchmark statistics

Generated: `2026-10-08T07:25:00+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **110**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 110 | 100% | 1378 ms | 2636 ms | 182.7 | 250.9 | 5.29 s | 8.21 s | 704 | $0.000475 |
| DeepSeek | 110 | 100% | 833 ms | 1175 ms | 237.1 | 257.1 | 3.93 s | 4.86 s | 728 | $0.000490 |
| Fireworks | 110 | 100% | 704 ms | 2952 ms | 96.2 | 177.8 | 8.29 s | 13.94 s | 706 | $0.000528 |
| HAI | 110 | 97% | 3563 ms | 28051 ms | 95.8 | 197.6 | 10.40 s | 101.54 s | 566 | ¥0.1532 |

## Latest run

Run `20261008T072447Z-499a1b4b` · `2026-10-08T07:24:47.740397+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37743249971)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1748 ms | 169.1 | 3.72 s | 280 | 332 | $0.000482 |
| DeepSeek | ok | stop | 812 ms | 231.1 | 3.36 s | 280 | 588 | $0.000790 |
| Fireworks | ok | stop | 315 ms | 171.2 | 3.67 s | 280 | 575 | $0.000441 |
| HAI | ok | stop | 4129 ms | 88.3 | 12.37 s | 291 | 722 | ¥0.1907 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
