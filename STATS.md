# Benchmark statistics

Generated: `2026-09-21T21:04:33+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **32**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 32 | 100% | 1128 ms | 1475 ms | 238.5 | 266.7 | 4.21 s | 5.89 s | 710 | $0.000472 |
| DeepSeek | 32 | 100% | 923 ms | 1130 ms | 239.7 | 258.5 | 3.87 s | 4.71 s | 694 | $0.000476 |
| Fireworks | 32 | 100% | 688 ms | 2074 ms | 97.3 | 149.5 | 8.35 s | 10.96 s | 720 | $0.000537 |
| HAI | 32 | 97% | 2923 ms | 28537 ms | 100.2 | 217.3 | 7.58 s | 105.97 s | 523 | ¥0.1429 |

## Latest run

Run `20260921T210421Z-5b6a8b2b` · `2026-09-21T21:04:21.407127+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35654955625)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1130 ms | 235.3 | 5.04 s | 277 | 919 | $0.000593 |
| DeepSeek | ok | stop | 968 ms | 232.1 | 4.16 s | 277 | 739 | $0.000485 |
| Fireworks | ok | stop | 652 ms | 85.6 | 9.80 s | 277 | 783 | $0.000578 |
| HAI | ok | stop | 6992 ms | 149.4 | 11.70 s | 288 | 694 | ¥0.1838 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
