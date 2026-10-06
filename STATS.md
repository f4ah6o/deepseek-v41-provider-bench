# Benchmark statistics

Generated: `2026-10-06T15:15:33+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **103**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 103 | 100% | 1381 ms | 2531 ms | 183.3 | 250.1 | 5.31 s | 8.38 s | 710 | $0.000473 |
| DeepSeek | 103 | 100% | 828 ms | 1163 ms | 237.3 | 257.7 | 3.93 s | 4.88 s | 727 | $0.000484 |
| Fireworks | 103 | 100% | 718 ms | 3124 ms | 94.1 | 173.0 | 8.53 s | 14.08 s | 709 | $0.000530 |
| HAI | 103 | 97% | 3479 ms | 27819 ms | 98.0 | 197.7 | 9.98 s | 96.24 s | 553 | ¥0.1502 |

## Latest run

Run `20261006T151204Z-3e16ab78` · `2026-10-06T15:12:04.041000+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37485367435)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 3844 ms | 158.7 | 8.65 s | 281 | 762 | $0.000499 |
| DeepSeek | ok | stop | 1831 ms | 237.2 | 4.94 s | 281 | 736 | $0.000484 |
| Fireworks | ok | stop | 526 ms | 199.9 | 4.61 s | 281 | 817 | $0.000601 |
| HAI | ok | stop | 130180 ms | 5.8 | 208.93 s | 292 | 458 | ¥0.1274 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
