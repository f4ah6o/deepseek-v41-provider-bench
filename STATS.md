# Benchmark statistics

Generated: `2026-10-01T05:53:40+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **79**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 79 | 100% | 1330 ms | 2169 ms | 208.7 | 252.0 | 5.04 s | 7.99 s | 710 | $0.000469 |
| DeepSeek | 79 | 100% | 845 ms | 1139 ms | 237.0 | 256.2 | 3.86 s | 4.69 s | 722 | $0.000482 |
| Fireworks | 79 | 100% | 677 ms | 2500 ms | 96.7 | 169.1 | 8.06 s | 12.86 s | 714 | $0.000533 |
| HAI | 79 | 97% | 3360 ms | 27872 ms | 100.1 | 205.6 | 9.78 s | 97.47 s | 556 | ¥0.1509 |

## Latest run

Run `20261001T055324Z-b6f97188` · `2026-10-01T05:53:24.874889+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36821932517)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1192 ms | 208.7 | 5.41 s | 278 | 880 | $0.000570 |
| DeepSeek | ok | stop | 582 ms | 238.9 | 3.89 s | 278 | 790 | $0.000516 |
| Fireworks | ok | stop | 3672 ms | 74.1 | 14.85 s | 278 | 828 | $0.000608 |
| HAI | ok | stop | 1723 ms | 173.1 | 4.90 s | 289 | 545 | ¥0.1481 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
