# Benchmark statistics

Generated: `2026-09-24T04:50:36+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **45**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 45 | 100% | 1178 ms | 1790 ms | 235.3 | 264.6 | 4.36 s | 7.58 s | 710 | $0.000468 |
| DeepSeek | 45 | 100% | 896 ms | 1130 ms | 237.9 | 259.0 | 3.80 s | 4.65 s | 692 | $0.000475 |
| Fireworks | 45 | 100% | 642 ms | 2271 ms | 99.1 | 179.7 | 7.81 s | 10.65 s | 706 | $0.000528 |
| HAI | 45 | 98% | 3018 ms | 29052 ms | 99.8 | 197.7 | 8.69 s | 102.76 s | 532 | ¥0.1451 |

## Latest run

Run `20260924T045029Z-5679640f` · `2026-09-24T04:50:29.405068+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35957338126)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1274 ms | 236.0 | 3.92 s | 281 | 624 | $0.000417 |
| DeepSeek | ok | stop | 673 ms | 245.3 | 3.37 s | 281 | 660 | $0.000438 |
| Fireworks | ok | stop | 1208 ms | 134.8 | 6.88 s | 281 | 765 | $0.000567 |
| HAI | ok | stop | 2497 ms | 197.7 | 4.57 s | 292 | 402 | ¥0.1140 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
