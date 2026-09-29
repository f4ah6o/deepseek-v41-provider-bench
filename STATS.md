# Benchmark statistics

Generated: `2026-09-29T20:47:12+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **73**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 73 | 100% | 1330 ms | 1993 ms | 218.3 | 253.4 | 4.78 s | 8.13 s | 705 | $0.000468 |
| DeepSeek | 73 | 100% | 881 ms | 1147 ms | 237.0 | 256.8 | 3.87 s | 4.70 s | 722 | $0.000481 |
| Fireworks | 73 | 100% | 652 ms | 2422 ms | 96.7 | 170.6 | 7.86 s | 12.81 s | 709 | $0.000530 |
| HAI | 73 | 97% | 3360 ms | 25469 ms | 100.2 | 217.3 | 9.16 s | 95.19 s | 556 | ¥0.1509 |

## Latest run

Run `20260929T204701Z-5a825963` · `2026-09-29T20:47:01.890291+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36628763559)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1717 ms | 185.3 | 3.88 s | 276 | 400 | $0.000281 |
| DeepSeek | ok | stop | 508 ms | 246.8 | 2.92 s | 276 | 595 | $0.000398 |
| Fireworks | ok | stop | 647 ms | 144.0 | 5.67 s | 276 | 724 | $0.000539 |
| HAI | ok | stop | 2093 ms | 96.6 | 9.86 s | 287 | 744 | ¥0.1958 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
