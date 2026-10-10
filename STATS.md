# Benchmark statistics

Generated: `2026-10-10T07:07:08+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **118**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 118 | 98% | 1372 ms | 2597 ms | 178.0 | 250.5 | 5.29 s | 8.06 s | 704 | $0.000476 |
| DeepSeek | 118 | 100% | 846 ms | 1168 ms | 237.2 | 256.3 | 3.92 s | 4.83 s | 724 | $0.000484 |
| Fireworks | 118 | 100% | 712 ms | 2755 ms | 96.7 | 182.4 | 8.07 s | 13.78 s | 706 | $0.000528 |
| HAI | 118 | 97% | 3563 ms | 27908 ms | 95.8 | 197.5 | 11.18 s | 98.28 s | 573 | ¥0.1553 |

## Latest run

Run `20261010T070701Z-99b79d3e` · `2026-10-10T07:07:01.168010+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/38033295449)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | http_error | — | — | — | 0.42 s | — | — | — |
| DeepSeek | ok | stop | 1111 ms | 234.6 | 3.76 s | 281 | 619 | $0.000414 |
| Fireworks | ok | stop | 520 ms | 129.6 | 6.49 s | 281 | 773 | $0.000572 |
| HAI | ok | stop | 2249 ms | 99.0 | 7.42 s | 292 | 503 | ¥0.1382 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
