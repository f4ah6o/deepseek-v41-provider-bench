# Benchmark statistics

Generated: `2026-10-06T00:49:49+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **101**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 101 | 100% | 1375 ms | 2217 ms | 184.9 | 250.2 | 5.27 s | 7.94 s | 705 | $0.000469 |
| DeepSeek | 101 | 100% | 824 ms | 1162 ms | 237.4 | 257.9 | 3.90 s | 4.81 s | 725 | $0.000484 |
| Fireworks | 101 | 100% | 718 ms | 3173 ms | 93.5 | 168.6 | 8.54 s | 14.12 s | 709 | $0.000530 |
| HAI | 101 | 97% | 3479 ms | 23837 ms | 98.0 | 197.7 | 9.98 s | 94.74 s | 560 | ¥0.1520 |

## Latest run

Run `20261006T004913Z-2a20088a` · `2026-10-06T00:49:13.196076+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37395953755)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1247 ms | 170.2 | 5.47 s | 279 | 719 | $0.000473 |
| DeepSeek | ok | stop | 763 ms | 243.7 | 3.45 s | 279 | 655 | $0.000435 |
| Fireworks | ok | stop | 268 ms | 325.3 | 2.40 s | 279 | 694 | $0.000519 |
| HAI | ok | stop | 4013 ms | 26.9 | 35.95 s | 290 | 856 | ¥0.2228 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
