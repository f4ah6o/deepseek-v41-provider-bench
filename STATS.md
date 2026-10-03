# Benchmark statistics

Generated: `2026-10-03T06:32:57+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **88**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 88 | 100% | 1344 ms | 2411 ms | 187.6 | 251.0 | 5.24 s | 8.25 s | 710 | $0.000476 |
| DeepSeek | 88 | 100% | 857 ms | 1153 ms | 237.1 | 255.9 | 3.90 s | 4.81 s | 720 | $0.000481 |
| Fireworks | 88 | 100% | 688 ms | 2611 ms | 96.4 | 167.8 | 8.20 s | 12.95 s | 717 | $0.000535 |
| HAI | 88 | 97% | 3324 ms | 26868 ms | 100.2 | 197.7 | 9.78 s | 95.58 s | 565 | ¥0.1531 |

## Latest run

Run `20261003T063246Z-8230b66f` · `2026-10-03T06:32:46.156977+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37103403238)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1369 ms | 168.5 | 5.99 s | 283 | 778 | $0.000509 |
| DeepSeek | ok | stop | 965 ms | 251.5 | 4.80 s | 283 | 964 | $0.000621 |
| Fireworks | ok | stop | 1622 ms | 75.4 | 10.97 s | 283 | 705 | $0.000528 |
| HAI | ok | stop | 3324 ms | 93.5 | 8.74 s | 294 | 501 | ¥0.1379 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
