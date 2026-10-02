# Benchmark statistics

Generated: `2026-10-02T15:49:14+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **85**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 85 | 100% | 1335 ms | 2477 ms | 195.7 | 251.2 | 5.13 s | 8.33 s | 705 | $0.000469 |
| DeepSeek | 85 | 100% | 868 ms | 1157 ms | 237.0 | 256.0 | 3.89 s | 4.80 s | 719 | $0.000481 |
| Fireworks | 85 | 100% | 682 ms | 2460 ms | 96.5 | 168.1 | 8.13 s | 12.84 s | 720 | $0.000536 |
| HAI | 85 | 96% | 3341 ms | 27568 ms | 100.2 | 197.7 | 9.81 s | 95.77 s | 569 | ¥0.1542 |

## Latest run

Run `20261002T154859Z-82f788e4` · `2026-10-02T15:48:59.909361+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37029599888)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1185 ms | 183.3 | 4.94 s | 281 | 688 | $0.000455 |
| DeepSeek | ok | stop | 1058 ms | 243.4 | 4.01 s | 281 | 719 | $0.000474 |
| Fireworks | ok | stop | 645 ms | 91.1 | 7.44 s | 281 | 619 | $0.000470 |
| HAI | ok | stop | 8823 ms | 101.9 | 14.24 s | 292 | 550 | ¥0.1495 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
