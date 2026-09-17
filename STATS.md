# Benchmark statistics

Generated: `2026-09-17T00:34:06+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **4**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 4 | 100% | 1239 ms | 1839 ms | 228.4 | 263.4 | 3.70 s | 7.74 s | 639 | $0.000425 |
| DeepSeek | 4 | 100% | 1133 ms | 1184 ms | 238.7 | 239.8 | 4.21 s | 4.80 s | 746 | $0.000489 |
| Fireworks | 4 | 100% | 1063 ms | 2211 ms | 128.4 | 145.3 | 7.51 s | 9.19 s | 730 | $0.000543 |
| HAI | 4 | 100% | 4442 ms | 20647 ms | 97.6 | 100.1 | 18.78 s | 78.50 s | 607 | ¥0.1630 |

## Latest run

Run `20260917T003238Z-8772fa06` · `2026-09-17T00:32:38.940842+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35166969583)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1901 ms | 103.5 | 8.42 s | 280 | 668 | $0.000443 |
| DeepSeek | ok | stop | 1188 ms | 208.1 | 4.89 s | 280 | 770 | $0.000504 |
| Fireworks | ok | stop | 595 ms | 146.8 | 5.51 s | 280 | 721 | $0.000537 |
| HAI | ok | stop | 6536 ms | 8.5 | 87.26 s | 291 | 687 | ¥0.1823 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
