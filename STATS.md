# Benchmark statistics

Generated: `2026-10-07T00:42:33+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **105**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 105 | 100% | 1375 ms | 2496 ms | 184.9 | 251.2 | 5.27 s | 8.33 s | 710 | $0.000473 |
| DeepSeek | 105 | 100% | 828 ms | 1163 ms | 237.2 | 257.5 | 3.93 s | 4.88 s | 728 | $0.000485 |
| Fireworks | 105 | 100% | 718 ms | 3075 ms | 95.4 | 179.7 | 8.35 s | 14.04 s | 709 | $0.000530 |
| HAI | 105 | 97% | 3479 ms | 27568 ms | 98.0 | 197.7 | 9.98 s | 95.77 s | 560 | ¥0.1520 |

## Latest run

Run `20261007T004225Z-d09a5073` · `2026-10-07T00:42:25.230870+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37553347101)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 980 ms | 258.9 | 3.70 s | 279 | 704 | $0.000464 |
| DeepSeek | ok | stop | 1154 ms | 227.0 | 4.73 s | 279 | 812 | $0.000529 |
| Fireworks | ok | stop | 523 ms | 193.9 | 3.48 s | 279 | 554 | $0.000427 |
| HAI | ok | stop | 1603 ms | 105.0 | 7.99 s | 290 | 666 | ¥0.1772 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
