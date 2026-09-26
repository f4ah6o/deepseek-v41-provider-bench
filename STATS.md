# Benchmark statistics

Generated: `2026-09-26T13:05:34+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **57**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 57 | 100% | 1213 ms | 2426 ms | 229.2 | 258.5 | 4.45 s | 7.77 s | 710 | $0.000469 |
| DeepSeek | 57 | 100% | 881 ms | 1162 ms | 236.3 | 258.2 | 3.86 s | 4.74 s | 697 | $0.000477 |
| Fireworks | 57 | 100% | 620 ms | 2443 ms | 98.4 | 175.0 | 7.67 s | 10.85 s | 709 | $0.000530 |
| HAI | 57 | 98% | 3404 ms | 28169 ms | 100.2 | 207.5 | 9.42 s | 97.87 s | 546 | ¥0.1485 |

## Latest run

Run `20260926T130524Z-acc9a5e5` · `2026-09-26T13:05:24.060890+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36243983736)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1329 ms | 155.6 | 5.23 s | 280 | 607 | $0.000406 |
| DeepSeek | ok | stop | 555 ms | 235.9 | 3.75 s | 280 | 753 | $0.000494 |
| Fireworks | ok | stop | 442 ms | 81.2 | 9.94 s | 280 | 771 | $0.000570 |
| HAI | ok | stop | 2265 ms | 166.2 | 5.65 s | 291 | 556 | ¥0.1509 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
