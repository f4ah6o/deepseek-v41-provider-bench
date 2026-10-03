# Benchmark statistics

Generated: `2026-10-03T19:58:42+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **91**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 91 | 100% | 1369 ms | 2392 ms | 185.3 | 250.9 | 5.23 s | 8.18 s | 705 | $0.000469 |
| DeepSeek | 91 | 100% | 834 ms | 1150 ms | 237.3 | 258.6 | 3.87 s | 4.81 s | 714 | $0.000480 |
| Fireworks | 91 | 100% | 689 ms | 2580 ms | 96.1 | 167.4 | 8.30 s | 13.18 s | 714 | $0.000533 |
| HAI | 91 | 97% | 3342 ms | 26169 ms | 100.2 | 197.7 | 9.81 s | 95.39 s | 569 | ¥0.1542 |

## Latest run

Run `20261003T195813Z-9bc337f1` · `2026-10-03T19:58:13.071025+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37149804177)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 2217 ms | 206.1 | 5.09 s | 280 | 591 | $0.000397 |
| DeepSeek | ok | stop | 692 ms | 260.9 | 2.80 s | 280 | 550 | $0.000372 |
| Fireworks | ok | stop | 718 ms | 52.9 | 13.02 s | 280 | 648 | $0.000489 |
| HAI | ok | stop | 3590 ms | 18.8 | 29.11 s | 291 | 478 | ¥0.1322 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
