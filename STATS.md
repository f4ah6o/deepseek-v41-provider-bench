# Benchmark statistics

Generated: `2026-10-04T09:47:51+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **94**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 94 | 100% | 1372 ms | 2339 ms | 187.6 | 250.7 | 5.24 s | 8.11 s | 701 | $0.000468 |
| DeepSeek | 94 | 100% | 830 ms | 1146 ms | 236.9 | 258.4 | 3.88 s | 4.84 s | 716 | $0.000480 |
| Fireworks | 94 | 100% | 700 ms | 2550 ms | 95.7 | 167.1 | 8.35 s | 13.37 s | 712 | $0.000532 |
| HAI | 94 | 97% | 3434 ms | 25469 ms | 100.1 | 197.7 | 9.86 s | 95.19 s | 565 | ¥0.1531 |

## Latest run

Run `20261004T094735Z-6f0171bd` · `2026-10-04T09:47:35.819911+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37193271791)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1495 ms | 160.0 | 5.40 s | 282 | 625 | $0.000417 |
| DeepSeek | ok | stop | 655 ms | 223.7 | 4.22 s | 282 | 797 | $0.000521 |
| Fireworks | ok | stop | 2015 ms | 51.7 | 15.73 s | 282 | 709 | $0.000530 |
| HAI | ok | stop | 4354 ms | 96.7 | 11.18 s | 293 | 649 | ¥0.1733 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
