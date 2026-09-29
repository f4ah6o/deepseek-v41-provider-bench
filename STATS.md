# Benchmark statistics

Generated: `2026-09-29T01:57:34+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **70**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 70 | 100% | 1306 ms | 2024 ms | 221.7 | 254.2 | 4.75 s | 7.84 s | 704 | $0.000468 |
| DeepSeek | 70 | 100% | 888 ms | 1151 ms | 236.9 | 256.9 | 3.87 s | 4.71 s | 718 | $0.000480 |
| Fireworks | 70 | 100% | 654 ms | 2436 ms | 96.8 | 171.3 | 7.84 s | 12.82 s | 712 | $0.000532 |
| HAI | 70 | 99% | 3360 ms | 25936 ms | 100.2 | 221.3 | 9.09 s | 95.32 s | 547 | ¥0.1487 |

## Latest run

Run `20260929T015722Z-6d06f97f` · `2026-09-29T01:57:22.653866+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36510303539)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1586 ms | 139.3 | 6.30 s | 283 | 656 | $0.000872 |
| DeepSeek | ok | stop | 1108 ms | 214.5 | 4.24 s | 283 | 671 | $0.000890 |
| Fireworks | ok | stop | 615 ms | 81.0 | 11.11 s | 283 | 847 | $0.000621 |
| HAI | ok | stop | 2005 ms | 161.8 | 5.29 s | 294 | 524 | ¥0.1434 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
