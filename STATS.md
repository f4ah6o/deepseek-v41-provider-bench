# Benchmark statistics

Generated: `2026-09-18T14:34:21+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **12**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 12 | 100% | 1135 ms | 1675 ms | 235.3 | 267.0 | 4.13 s | 7.37 s | 678 | $0.000449 |
| DeepSeek | 12 | 100% | 943 ms | 1174 ms | 237.4 | 254.6 | 3.93 s | 4.71 s | 693 | $0.000476 |
| Fireworks | 12 | 100% | 688 ms | 1752 ms | 97.3 | 167.5 | 7.87 s | 10.01 s | 712 | $0.000531 |
| HAI | 12 | 92% | 2854 ms | 19851 ms | 95.8 | 137.9 | 8.74 s | 77.07 s | 543 | ¥0.1476 |

## Latest run

Run `20260918T143120Z-b107bb01` · `2026-09-18T14:31:20.968281+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35356721119)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1213 ms | 143.2 | 6.50 s | 281 | 749 | $0.000492 |
| DeepSeek | ok | stop | 758 ms | 219.0 | 3.58 s | 281 | 618 | $0.000413 |
| Fireworks | ok | stop | 688 ms | 152.9 | 5.52 s | 281 | 739 | $0.000550 |
| HAI | transport_error | — | — | — | 180.70 s | — | — | — |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
