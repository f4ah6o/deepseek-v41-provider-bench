# Benchmark statistics

Generated: `2026-10-10T00:50:56+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **117**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 117 | 99% | 1372 ms | 2597 ms | 178.0 | 250.5 | 5.29 s | 8.06 s | 704 | $0.000476 |
| DeepSeek | 117 | 100% | 845 ms | 1169 ms | 237.3 | 256.4 | 3.93 s | 4.83 s | 725 | $0.000485 |
| Fireworks | 117 | 100% | 718 ms | 2780 ms | 96.7 | 182.6 | 8.08 s | 13.80 s | 706 | $0.000528 |
| HAI | 117 | 97% | 3565 ms | 27926 ms | 95.8 | 197.5 | 11.22 s | 98.69 s | 574 | ¥0.1554 |

## Latest run

Run `20261010T005051Z-2df6a0bf` · `2026-10-10T00:50:51.111092+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/38010776008)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | http_error | — | — | — | 0.40 s | — | — | — |
| DeepSeek | ok | stop | 1010 ms | 208.3 | 4.41 s | 281 | 707 | $0.000466 |
| Fireworks | ok | stop | 464 ms | 144.4 | 4.91 s | 281 | 641 | $0.000485 |
| HAI | ok | stop | 2068 ms | 175.4 | 4.99 s | 292 | 501 | ¥0.1378 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
