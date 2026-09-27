# Benchmark statistics

Generated: `2026-09-27T18:24:01+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **64**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 64 | 100% | 1247 ms | 2092 ms | 224.7 | 255.7 | 4.56 s | 7.72 s | 698 | $0.000466 |
| DeepSeek | 64 | 100% | 881 ms | 1159 ms | 237.3 | 257.6 | 3.84 s | 4.72 s | 708 | $0.000479 |
| Fireworks | 64 | 100% | 647 ms | 2360 ms | 97.3 | 172.8 | 7.74 s | 12.60 s | 708 | $0.000529 |
| HAI | 64 | 98% | 3447 ms | 27335 ms | 100.2 | 233.0 | 9.16 s | 95.71 s | 547 | ¥0.1487 |

## Latest run

Run `20260927T182351Z-90c7c3a1` · `2026-09-27T18:23:51.733934+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36340480248)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1808 ms | 158.5 | 6.21 s | 284 | 694 | $0.000459 |
| DeepSeek | ok | stop | 894 ms | 252.9 | 3.78 s | 284 | 729 | $0.000480 |
| Fireworks | ok | stop | 444 ms | 104.7 | 6.46 s | 284 | 630 | $0.000478 |
| HAI | ok | stop | 2022 ms | 103.5 | 9.16 s | 295 | 736 | ¥0.1943 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
