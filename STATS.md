# Benchmark statistics

Generated: `2026-09-21T10:44:10+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **30**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 30 | 100% | 1131 ms | 1478 ms | 238.5 | 266.7 | 4.21 s | 6.00 s | 710 | $0.000472 |
| DeepSeek | 30 | 100% | 901 ms | 1136 ms | 239.7 | 258.7 | 3.83 s | 4.74 s | 690 | $0.000466 |
| Fireworks | 30 | 100% | 689 ms | 2130 ms | 97.3 | 150.1 | 8.35 s | 11.00 s | 720 | $0.000537 |
| HAI | 30 | 97% | 2923 ms | 28684 ms | 99.4 | 221.3 | 7.58 s | 108.26 s | 523 | ¥0.1429 |

## Latest run

Run `20260921T104400Z-c3bfb242` · `2026-09-21T10:44:00.363647+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35590281940)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 977 ms | 250.2 | 3.98 s | 281 | 751 | $0.000493 |
| DeepSeek | ok | stop | 821 ms | 255.7 | 3.41 s | 281 | 659 | $0.000438 |
| Fireworks | ok | stop | 995 ms | 81.2 | 9.87 s | 281 | 721 | $0.000538 |
| HAI | ok | stop | 1734 ms | 138.4 | 7.00 s | 292 | 720 | ¥0.1903 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
