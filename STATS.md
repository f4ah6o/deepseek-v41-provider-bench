# Benchmark statistics

Generated: `2026-10-06T20:20:25+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **104**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 104 | 100% | 1378 ms | 2513 ms | 184.1 | 250.0 | 5.29 s | 8.35 s | 710 | $0.000475 |
| DeepSeek | 104 | 100% | 826 ms | 1163 ms | 237.2 | 257.6 | 3.93 s | 4.88 s | 728 | $0.000484 |
| Fireworks | 104 | 100% | 719 ms | 3099 ms | 94.7 | 172.9 | 8.44 s | 14.06 s | 709 | $0.000530 |
| HAI | 104 | 97% | 3511 ms | 27801 ms | 96.7 | 197.7 | 10.01 s | 95.84 s | 556 | ¥0.1509 |

## Latest run

Run `20261006T201954Z-e8f14d1a` · `2026-10-06T20:19:54.659148+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37525599366)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 834 ms | 198.5 | 4.64 s | 279 | 754 | $0.000494 |
| DeepSeek | ok | stop | 741 ms | 232.1 | 4.25 s | 279 | 813 | $0.000530 |
| Fireworks | ok | stop | 1169 ms | 169.4 | 5.86 s | 279 | 795 | $0.000586 |
| HAI | ok | stop | 3567 ms | 28.9 | 30.82 s | 290 | 784 | ¥0.2056 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
