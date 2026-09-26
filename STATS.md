# Benchmark statistics

Generated: `2026-09-26T07:41:31+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **56**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 56 | 100% | 1210 ms | 2502 ms | 229.3 | 259.0 | 4.45 s | 7.78 s | 710 | $0.000472 |
| DeepSeek | 56 | 100% | 889 ms | 1163 ms | 236.6 | 258.3 | 3.86 s | 4.75 s | 696 | $0.000476 |
| Fireworks | 56 | 100% | 631 ms | 2458 ms | 98.8 | 175.4 | 7.64 s | 10.87 s | 708 | $0.000529 |
| HAI | 56 | 98% | 3447 ms | 28243 ms | 100.2 | 209.5 | 9.78 s | 98.28 s | 545 | ¥0.1483 |

## Latest run

Run `20260926T074054Z-56b602ac` · `2026-09-26T07:40:54.328365+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36227510296)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1483 ms | 175.3 | 6.32 s | 284 | 806 | $0.000526 |
| DeepSeek | ok | stop | 1245 ms | 215.9 | 4.72 s | 284 | 750 | $0.000493 |
| Fireworks | ok | stop | 972 ms | 150.3 | 5.69 s | 284 | 709 | $0.000530 |
| HAI | ok | stop | 3563 ms | 84.1 | 36.95 s | 374 | 2730 | ¥0.6776 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
