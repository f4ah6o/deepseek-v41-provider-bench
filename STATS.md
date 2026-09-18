# Benchmark statistics

Generated: `2026-09-18T21:41:35+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **14**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 14 | 100% | 1135 ms | 1634 ms | 236.8 | 267.0 | 4.06 s | 7.17 s | 678 | $0.000449 |
| DeepSeek | 14 | 100% | 943 ms | 1172 ms | 238.7 | 254.4 | 3.93 s | 4.67 s | 694 | $0.000476 |
| Fireworks | 14 | 100% | 688 ms | 1638 ms | 108.6 | 164.2 | 7.20 s | 9.97 s | 712 | $0.000531 |
| HAI | 14 | 93% | 2854 ms | 25591 ms | 95.6 | 134.2 | 8.74 s | 75.03 s | 543 | ¥0.1476 |

## Latest run

Run `20260918T214128Z-394c82d0` · `2026-09-18T21:41:28.006289+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35398006521)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1097 ms | 244.8 | 4.05 s | 277 | 711 | $0.000468 |
| DeepSeek | ok | stop | 824 ms | 245.7 | 3.64 s | 277 | 692 | $0.000457 |
| Fireworks | ok | stop | 438 ms | 131.2 | 6.42 s | 277 | 784 | $0.000578 |
| HAI | ok | stop | 2329 ms | 95.2 | 6.72 s | 288 | 415 | ¥0.1169 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
