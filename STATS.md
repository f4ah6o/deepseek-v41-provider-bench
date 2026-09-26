# Benchmark statistics

Generated: `2026-09-26T01:34:27+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **55**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 55 | 100% | 1207 ms | 2577 ms | 229.4 | 259.5 | 4.45 s | 7.79 s | 710 | $0.000469 |
| DeepSeek | 55 | 100% | 881 ms | 1144 ms | 236.9 | 258.3 | 3.86 s | 4.71 s | 695 | $0.000475 |
| Fireworks | 55 | 100% | 620 ms | 2473 ms | 98.4 | 175.8 | 7.67 s | 10.89 s | 706 | $0.000528 |
| HAI | 55 | 98% | 3404 ms | 28316 ms | 100.2 | 211.5 | 9.42 s | 98.69 s | 544 | ¥0.1480 |

## Latest run

Run `20260926T013356Z-8edd84e6` · `2026-09-26T01:33:56.763998+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36208846158)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1484 ms | 206.2 | 3.02 s | 280 | 317 | $0.000232 |
| DeepSeek | ok | stop | 783 ms | 232.2 | 3.56 s | 280 | 644 | $0.000428 |
| Fireworks | ok | stop | 606 ms | 94.1 | 6.62 s | 280 | 566 | $0.000435 |
| HAI | ok | stop | 4141 ms | 16.8 | 30.89 s | 291 | 447 | ¥0.1247 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
