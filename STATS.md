# Benchmark statistics

Generated: `2026-09-16T18:54:38+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **2**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 2 | 100% | 1197 ms | 1461 ms | 228.4 | 239.2 | 3.70 s | 3.85 s | 562 | $0.000379 |
| DeepSeek | 2 | 100% | 1086 ms | 1155 ms | 239.7 | 239.9 | 4.16 s | 4.26 s | 734 | $0.000482 |
| Fireworks | 2 | 100% | 1063 ms | 1219 ms | 116.1 | 134.7 | 7.51 s | 8.85 s | 720 | $0.000537 |
| HAI | 2 | 100% | 12742 ms | 22098 ms | 98.0 | 100.0 | 17.67 s | 27.71 s | 478 | ¥0.1319 |

## Latest run

Run `20260916T185429Z-f7e89361` · `2026-09-16T18:54:29.548688+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35137298438)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 903 ms | 240.4 | 3.55 s | 278 | 625 | $0.000417 |
| DeepSeek | ok | stop | 1163 ms | 239.9 | 4.05 s | 278 | 689 | $0.000455 |
| Fireworks | ok | stop | 1236 ms | 95.4 | 9.00 s | 278 | 739 | $0.000549 |
| HAI | ok | stop | 2348 ms | 100.2 | 6.52 s | 289 | 412 | ¥0.1162 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
