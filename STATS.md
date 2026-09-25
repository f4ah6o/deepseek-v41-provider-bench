# Benchmark statistics

Generated: `2026-09-25T13:47:37+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **52**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 52 | 100% | 1202 ms | 1865 ms | 232.7 | 261.0 | 4.43 s | 7.82 s | 710 | $0.000472 |
| DeepSeek | 52 | 100% | 881 ms | 1118 ms | 237.1 | 258.5 | 3.83 s | 4.74 s | 698 | $0.000477 |
| Fireworks | 52 | 100% | 647 ms | 2518 ms | 97.9 | 177.0 | 7.84 s | 10.96 s | 713 | $0.000532 |
| HAI | 52 | 98% | 3113 ms | 28537 ms | 100.2 | 217.3 | 8.86 s | 99.91 s | 547 | ¥0.1487 |

## Latest run

Run `20260925T134715Z-5160e326` · `2026-09-25T13:47:15.657542+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36143167474)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1722 ms | 155.7 | 6.46 s | 278 | 737 | $0.000484 |
| DeepSeek | ok | stop | 911 ms | 243.0 | 3.76 s | 278 | 691 | $0.000456 |
| Fireworks | ok | stop | 1034 ms | 86.1 | 7.67 s | 278 | 571 | $0.000438 |
| HAI | ok | stop | 14044 ms | 105.4 | 21.66 s | 289 | 746 | ¥0.1964 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
