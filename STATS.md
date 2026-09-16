# Benchmark statistics

Generated: `2026-09-16T22:10:56+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **3**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 3 | 100% | 986 ms | 1440 ms | 240.4 | 264.8 | 3.55 s | 3.83 s | 625 | $0.000417 |
| DeepSeek | 3 | 100% | 1102 ms | 1157 ms | 239.4 | 239.8 | 4.14 s | 4.26 s | 722 | $0.000475 |
| Fireworks | 3 | 100% | 1236 ms | 2269 ms | 120.0 | 135.1 | 9.00 s | 9.20 s | 739 | $0.000549 |
| HAI | 3 | 100% | 2348 ms | 21058 ms | 99.4 | 100.1 | 8.74 s | 26.81 s | 543 | ¥0.1476 |

## Latest run

Run `20260916T221046Z-e7d55376` · `2026-09-16T22:10:46.619395+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35156330449)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 986 ms | 267.5 | 3.50 s | 277 | 653 | $0.000433 |
| DeepSeek | ok | stop | 1102 ms | 237.9 | 4.14 s | 277 | 722 | $0.000475 |
| Fireworks | ok | stop | 2384 ms | 120.0 | 9.22 s | 277 | 820 | $0.000602 |
| HAI | ok | stop | 1963 ms | 99.4 | 8.74 s | 288 | 671 | ¥0.1783 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
