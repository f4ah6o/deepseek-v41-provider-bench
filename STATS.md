# Benchmark statistics

Generated: `2026-10-10T18:35:54+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **120**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 120 | 97% | 1372 ms | 2597 ms | 178.0 | 250.5 | 5.29 s | 8.06 s | 704 | $0.000476 |
| DeepSeek | 120 | 100% | 847 ms | 1184 ms | 237.3 | 256.1 | 3.92 s | 4.82 s | 721 | $0.000484 |
| Fireworks | 120 | 100% | 719 ms | 3183 ms | 96.8 | 182.0 | 8.07 s | 13.74 s | 706 | $0.000528 |
| HAI | 120 | 98% | 3563 ms | 27872 ms | 96.6 | 197.4 | 11.18 s | 97.47 s | 573 | ¥0.1553 |

## Latest run

Run `20261010T183545Z-f119fbb3` · `2026-10-10T18:35:45.192048+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/38076397811)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | http_error | — | — | — | 0.66 s | — | — | — |
| DeepSeek | ok | stop | 847 ms | 237.3 | 3.46 s | 280 | 619 | $0.000413 |
| Fireworks | ok | stop | 1220 ms | 118.6 | 7.37 s | 280 | 730 | $0.000543 |
| HAI | ok | stop | 2004 ms | 102.6 | 9.20 s | 291 | 735 | ¥0.1939 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
