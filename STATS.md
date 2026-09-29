# Benchmark statistics

Generated: `2026-09-29T08:34:45+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **71**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 71 | 100% | 1329 ms | 2013 ms | 221.0 | 253.9 | 4.78 s | 7.83 s | 705 | $0.000468 |
| DeepSeek | 71 | 100% | 881 ms | 1150 ms | 236.9 | 256.8 | 3.87 s | 4.70 s | 722 | $0.000481 |
| Fireworks | 71 | 100% | 656 ms | 2431 ms | 96.7 | 171.0 | 7.86 s | 12.82 s | 709 | $0.000530 |
| HAI | 71 | 97% | 3360 ms | 25936 ms | 100.2 | 221.3 | 9.09 s | 95.32 s | 547 | ¥0.1487 |

## Latest run

Run `20260929T083025Z-5df6dcea` · `2026-09-29T08:30:25.253730+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36543118610)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1432 ms | 136.5 | 7.10 s | 278 | 773 | $0.001011 |
| DeepSeek | ok | stop | 769 ms | 232.4 | 3.95 s | 278 | 739 | $0.000970 |
| Fireworks | ok | stop | 1311 ms | 67.3 | 11.49 s | 278 | 685 | $0.000513 |
| HAI | transport_error | — | — | — | 260.27 s | — | — | — |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
