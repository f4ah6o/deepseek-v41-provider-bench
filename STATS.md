# Benchmark statistics

Generated: `2026-10-11T01:53:40+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **122**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 122 | 95% | 1372 ms | 2597 ms | 178.0 | 250.5 | 5.29 s | 8.06 s | 704 | $0.000476 |
| DeepSeek | 122 | 100% | 848 ms | 1183 ms | 237.2 | 256.0 | 3.93 s | 4.94 s | 724 | $0.000484 |
| Fireworks | 122 | 100% | 719 ms | 3149 ms | 96.9 | 181.8 | 8.03 s | 13.70 s | 706 | $0.000527 |
| HAI | 122 | 98% | 3534 ms | 27837 ms | 95.8 | 197.4 | 11.18 s | 96.65 s | 576 | ¥0.1555 |

## Latest run

Run `20261011T015331Z-a915d124` · `2026-10-11T01:53:31.664885+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/38103334629)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | http_error | — | — | — | 0.37 s | — | — | — |
| DeepSeek | ok | stop | 887 ms | 191.5 | 6.18 s | 280 | 1013 | $0.000650 |
| Fireworks | ok | stop | 488 ms | 160.2 | 4.30 s | 280 | 610 | $0.000464 |
| HAI | ok | stop | 1890 ms | 89.5 | 8.61 s | 291 | 598 | ¥0.1610 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
