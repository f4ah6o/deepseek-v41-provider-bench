# Benchmark statistics

Generated: `2026-09-23T16:58:17+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **42**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 42 | 100% | 1141 ms | 1817 ms | 235.8 | 266.1 | 4.32 s | 7.01 s | 710 | $0.000469 |
| DeepSeek | 42 | 100% | 905 ms | 1135 ms | 238.7 | 259.2 | 3.79 s | 4.67 s | 690 | $0.000468 |
| Fireworks | 42 | 100% | 647 ms | 2355 ms | 98.3 | 180.9 | 7.84 s | 10.74 s | 700 | $0.000524 |
| HAI | 42 | 98% | 2923 ms | 29273 ms | 100.2 | 197.7 | 8.64 s | 103.98 s | 523 | ¥0.1429 |

## Latest run

Run `20260923T165807Z-32ecd874` · `2026-09-23T16:58:07.361700+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35892375072)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1647 ms | 154.4 | 6.23 s | 278 | 703 | $0.000463 |
| DeepSeek | ok | stop | 904 ms | 249.8 | 3.72 s | 278 | 700 | $0.000462 |
| Fireworks | ok | stop | 489 ms | 90.3 | 7.81 s | 278 | 661 | $0.000497 |
| HAI | ok | stop | 6014 ms | 100.2 | 10.40 s | 289 | 435 | ¥0.1217 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
