# Benchmark statistics

Generated: `2026-10-10T13:41:23+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **119**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 119 | 97% | 1372 ms | 2597 ms | 178.0 | 250.5 | 5.29 s | 8.06 s | 704 | $0.000476 |
| DeepSeek | 119 | 100% | 847 ms | 1184 ms | 237.3 | 256.2 | 3.93 s | 4.82 s | 722 | $0.000484 |
| Fireworks | 119 | 100% | 718 ms | 3192 ms | 96.7 | 182.2 | 8.08 s | 13.76 s | 706 | $0.000528 |
| HAI | 119 | 97% | 3565 ms | 27890 ms | 96.2 | 197.5 | 11.22 s | 97.87 s | 573 | ¥0.1550 |

## Latest run

Run `20261010T134111Z-661cd0c6` · `2026-10-10T13:41:11.070793+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/38056658433)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | http_error | — | — | — | 0.49 s | — | — | — |
| DeepSeek | ok | stop | 1289 ms | 239.5 | 4.19 s | 280 | 679 | $0.000449 |
| Fireworks | ok | stop | 3934 ms | 111.6 | 9.90 s | 280 | 666 | $0.000501 |
| HAI | ok | stop | 7334 ms | 106.2 | 12.42 s | 291 | 533 | ¥0.1454 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
