# Benchmark statistics

Generated: `2026-10-01T23:12:28+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **82**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 82 | 100% | 1332 ms | 2544 ms | 201.0 | 251.4 | 5.18 s | 8.40 s | 708 | $0.000469 |
| DeepSeek | 82 | 100% | 857 ms | 1161 ms | 237.1 | 256.0 | 3.87 s | 4.72 s | 708 | $0.000480 |
| Fireworks | 82 | 100% | 685 ms | 2475 ms | 96.6 | 168.5 | 8.20 s | 12.84 s | 720 | $0.000537 |
| HAI | 82 | 98% | 3341 ms | 27819 ms | 100.1 | 199.7 | 9.81 s | 96.24 s | 569 | ¥0.1542 |

## Latest run

Run `20261001T231218Z-d915a188` · `2026-10-01T23:12:18.396634+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36939495021)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1141 ms | 195.7 | 5.31 s | 278 | 815 | $0.000531 |
| DeepSeek | ok | stop | 587 ms | 244.1 | 3.15 s | 278 | 625 | $0.000417 |
| Fireworks | ok | stop | 1763 ms | 114.4 | 9.60 s | 278 | 897 | $0.000653 |
| HAI | ok | stop | 2388 ms | 104.7 | 9.95 s | 289 | 789 | ¥0.2067 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
