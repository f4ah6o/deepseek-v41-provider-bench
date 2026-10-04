# Benchmark statistics

Generated: `2026-10-04T15:22:58+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **95**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 95 | 100% | 1375 ms | 2322 ms | 189.8 | 250.6 | 5.25 s | 8.09 s | 703 | $0.000468 |
| DeepSeek | 95 | 100% | 831 ms | 1144 ms | 237.0 | 258.3 | 3.89 s | 4.84 s | 719 | $0.000481 |
| Fireworks | 95 | 100% | 702 ms | 2648 ms | 95.4 | 167.0 | 8.35 s | 13.61 s | 714 | $0.000533 |
| HAI | 95 | 97% | 3440 ms | 25236 ms | 99.8 | 197.7 | 9.90 s | 95.13 s | 560 | ¥0.1520 |

## Latest run

Run `20261004T152233Z-230491c7` · `2026-10-04T15:22:33.152106+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37212741786)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1658 ms | 190.0 | 5.59 s | 281 | 747 | $0.000490 |
| DeepSeek | ok | stop | 937 ms | 242.8 | 4.31 s | 281 | 814 | $0.000531 |
| Fireworks | ok | stop | 2634 ms | 50.0 | 16.90 s | 281 | 714 | $0.000533 |
| HAI | ok | stop | 4450 ms | 21.6 | 25.43 s | 292 | 453 | ¥0.1262 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
