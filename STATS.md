# Benchmark statistics

Generated: `2026-10-09T20:55:09+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **116**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 116 | 100% | 1372 ms | 2597 ms | 178.0 | 250.5 | 5.29 s | 8.06 s | 704 | $0.000476 |
| DeepSeek | 116 | 100% | 840 ms | 1170 ms | 237.3 | 256.5 | 3.92 s | 4.83 s | 726 | $0.000486 |
| Fireworks | 116 | 100% | 719 ms | 2804 ms | 96.6 | 182.7 | 8.11 s | 13.82 s | 706 | $0.000528 |
| HAI | 116 | 97% | 3567 ms | 27944 ms | 95.8 | 197.5 | 11.26 s | 99.09 s | 576 | ¥0.1555 |

## Latest run

Run `20261009T205435Z-26c3fae6` · `2026-10-09T20:54:35.479678+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37990078020)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1275 ms | 170.6 | 6.06 s | 281 | 816 | $0.000532 |
| DeepSeek | ok | stop | 763 ms | 250.6 | 3.47 s | 281 | 677 | $0.000448 |
| Fireworks | ok | stop | 1168 ms | 113.6 | 8.08 s | 281 | 785 | $0.000580 |
| HAI | ok | stop | 3318 ms | 18.7 | 34.17 s | 292 | 577 | ¥0.1560 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
