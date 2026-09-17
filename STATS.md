# Benchmark statistics

Generated: `2026-09-17T11:41:23+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **6**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 6 | 100% | 1193 ms | 1798 ms | 227.7 | 260.7 | 4.03 s | 7.43 s | 660 | $0.000438 |
| DeepSeek | 6 | 100% | 1056 ms | 1182 ms | 231.9 | 239.8 | 4.21 s | 4.74 s | 710 | $0.000489 |
| Fireworks | 6 | 100% | 789 ms | 2097 ms | 107.7 | 144.3 | 8.33 s | 9.16 s | 712 | $0.000531 |
| HAI | 6 | 100% | 2391 ms | 18987 ms | 99.8 | 142.7 | 8.03 s | 72.65 s | 607 | ¥0.1630 |

## Latest run

Run `20260917T114114Z-7b79672a` · `2026-09-17T11:41:14.960190+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35216979321)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1204 ms | 234.3 | 4.19 s | 278 | 689 | $0.000455 |
| DeepSeek | ok | stop | 940 ms | 225.9 | 3.80 s | 278 | 646 | $0.000429 |
| Fireworks | ok | stop | 597 ms | 92.5 | 8.13 s | 278 | 697 | $0.000521 |
| HAI | ok | stop | 1715 ms | 101.7 | 6.78 s | 289 | 512 | ¥0.1402 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
