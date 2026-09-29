# Benchmark statistics

Generated: `2026-09-29T15:51:45+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **72**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 72 | 100% | 1329 ms | 2004 ms | 219.7 | 253.7 | 4.88 s | 8.16 s | 708 | $0.000469 |
| DeepSeek | 72 | 100% | 888 ms | 1148 ms | 236.9 | 256.9 | 3.90 s | 4.70 s | 724 | $0.000481 |
| Fireworks | 72 | 100% | 654 ms | 2427 ms | 96.7 | 170.8 | 7.93 s | 12.82 s | 708 | $0.000529 |
| HAI | 72 | 97% | 3404 ms | 25702 ms | 100.9 | 219.3 | 9.12 s | 95.26 s | 552 | ¥0.1498 |

## Latest run

Run `20260929T155133Z-b01a96ff` · `2026-09-29T15:51:33.768664+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36593367824)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1906 ms | 141.2 | 9.28 s | 277 | 1041 | $0.000666 |
| DeepSeek | ok | stop | 898 ms | 256.0 | 4.34 s | 277 | 881 | $0.000570 |
| Fireworks | ok | stop | 569 ms | 80.4 | 8.68 s | 277 | 652 | $0.000491 |
| HAI | ok | stop | 5591 ms | 105.7 | 11.38 s | 288 | 608 | ¥0.1632 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
