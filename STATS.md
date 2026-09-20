# Benchmark statistics

Generated: `2026-09-20T11:32:34+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **24**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 24 | 100% | 1162 ms | 1487 ms | 238.0 | 266.7 | 4.21 s | 6.33 s | 690 | $0.000456 |
| DeepSeek | 24 | 100% | 941 ms | 1154 ms | 237.6 | 257.1 | 3.90 s | 4.84 s | 694 | $0.000476 |
| Fireworks | 24 | 100% | 689 ms | 2299 ms | 98.3 | 152.0 | 7.87 s | 11.13 s | 700 | $0.000523 |
| HAI | 24 | 96% | 2482 ms | 27335 ms | 100.2 | 233.0 | 7.33 s | 85.23 s | 523 | ¥0.1429 |

## Latest run

Run `20260920T113202Z-c592e1a6` · `2026-09-20T11:32:02.328054+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35508093030)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1103 ms | 232.5 | 5.38 s | 283 | 995 | $0.000639 |
| DeepSeek | ok | stop | 906 ms | 243.1 | 4.08 s | 283 | 770 | $0.000504 |
| Fireworks | ok | stop | 580 ms | 105.4 | 6.44 s | 283 | 617 | $0.000469 |
| HAI | ok | stop | 27801 ms | 89.8 | 32.26 s | 294 | 397 | ¥0.1129 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
