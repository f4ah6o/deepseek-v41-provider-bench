# Benchmark statistics

Generated: `2026-10-07T14:35:00+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **107**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 107 | 100% | 1375 ms | 2461 ms | 183.3 | 251.1 | 5.31 s | 8.28 s | 705 | $0.000473 |
| DeepSeek | 107 | 100% | 831 ms | 1177 ms | 237.2 | 257.3 | 3.94 s | 4.87 s | 729 | $0.000488 |
| Fireworks | 107 | 100% | 718 ms | 3026 ms | 96.1 | 178.9 | 8.34 s | 14.00 s | 709 | $0.000530 |
| HAI | 107 | 97% | 3523 ms | 28104 ms | 96.6 | 197.6 | 10.09 s | 102.76 s | 560 | ¥0.1520 |

## Latest run

Run `20261007T143301Z-bd78d0b5` · `2026-10-07T14:33:01.922058+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37637596919)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1269 ms | 134.0 | 5.90 s | 277 | 620 | $0.000414 |
| DeepSeek | ok | stop | 1303 ms | 228.3 | 4.63 s | 277 | 759 | $0.000497 |
| Fireworks | ok | stop | 306 ms | 160.2 | 4.72 s | 277 | 706 | $0.000527 |
| HAI | ok | stop | 74940 ms | 11.9 | 118.52 s | 288 | 519 | ¥0.1418 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
