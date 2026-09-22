# Benchmark statistics

Generated: `2026-09-22T14:53:59+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **36**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 36 | 100% | 1114 ms | 1593 ms | 237.7 | 266.6 | 4.21 s | 6.98 s | 710 | $0.000472 |
| DeepSeek | 36 | 100% | 908 ms | 1117 ms | 239.7 | 259.6 | 3.83 s | 4.64 s | 690 | $0.000476 |
| Fireworks | 36 | 100% | 685 ms | 1961 ms | 97.3 | 168.1 | 8.07 s | 10.87 s | 720 | $0.000537 |
| HAI | 36 | 97% | 2923 ms | 36120 ms | 95.8 | 209.5 | 8.74 s | 108.01 s | 520 | ¥0.1422 |

## Latest run

Run `20260922T145349Z-e8a6934f` · `2026-09-22T14:53:49.262987+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35743496998)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 812 ms | 222.4 | 4.55 s | 280 | 830 | $0.000540 |
| DeepSeek | ok | stop | 915 ms | 240.2 | 2.56 s | 280 | 395 | $0.000279 |
| Fireworks | ok | stop | 642 ms | 96.9 | 7.86 s | 280 | 699 | $0.000523 |
| HAI | ok | stop | 1992 ms | 60.8 | 9.84 s | 291 | 469 | ¥0.1300 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
