# Benchmark statistics

Generated: `2026-10-02T08:38:48+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **84**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 84 | 100% | 1336 ms | 2499 ms | 201.0 | 251.3 | 5.18 s | 8.35 s | 708 | $0.000472 |
| DeepSeek | 84 | 100% | 857 ms | 1159 ms | 236.9 | 256.0 | 3.88 s | 4.80 s | 718 | $0.000481 |
| Fireworks | 84 | 100% | 685 ms | 2465 ms | 96.6 | 168.2 | 8.20 s | 12.84 s | 720 | $0.000537 |
| HAI | 84 | 96% | 3322 ms | 27801 ms | 100.2 | 197.7 | 9.78 s | 95.84 s | 573 | ¥0.1553 |

## Latest run

Run `20261002T083653Z-bada0ca0` · `2026-10-02T08:36:53.108012+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36985006017)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 2097 ms | 238.8 | 4.66 s | 284 | 611 | $0.000818 |
| DeepSeek | ok | stop | 1128 ms | 222.3 | 5.16 s | 284 | 895 | $0.001159 |
| Fireworks | ok | stop | 461 ms | 118.3 | 6.22 s | 284 | 681 | $0.000512 |
| HAI | transport_error | — | — | — | 115.50 s | — | — | — |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
