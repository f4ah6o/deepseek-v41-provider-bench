# Benchmark statistics

Generated: `2026-09-22T18:54:50+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **37**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 37 | 100% | 1125 ms | 1593 ms | 238.1 | 266.6 | 4.23 s | 6.88 s | 710 | $0.000468 |
| DeepSeek | 37 | 100% | 906 ms | 1114 ms | 239.4 | 259.5 | 3.80 s | 4.62 s | 689 | $0.000475 |
| Fireworks | 37 | 100% | 682 ms | 1933 ms | 97.4 | 175.9 | 8.01 s | 10.85 s | 720 | $0.000536 |
| HAI | 37 | 97% | 2889 ms | 34979 ms | 97.6 | 207.5 | 8.18 s | 107.33 s | 522 | ¥0.1426 |

## Latest run

Run `20260922T185443Z-6b99712b` · `2026-09-22T18:54:43.607408+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35770295784)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1516 ms | 248.5 | 4.27 s | 277 | 681 | $0.000450 |
| DeepSeek | ok | stop | 881 ms | 225.9 | 3.72 s | 277 | 641 | $0.000426 |
| Fireworks | ok | stop | 426 ms | 212.5 | 3.64 s | 277 | 679 | $0.000509 |
| HAI | ok | stop | 1949 ms | 132.0 | 6.36 s | 288 | 576 | ¥0.1555 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
