# Benchmark statistics

Generated: `2026-09-27T13:58:26+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **63**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 63 | 100% | 1242 ms | 2103 ms | 225.2 | 255.9 | 4.55 s | 7.72 s | 703 | $0.000468 |
| DeepSeek | 63 | 100% | 881 ms | 1160 ms | 237.3 | 257.7 | 3.86 s | 4.72 s | 703 | $0.000478 |
| Fireworks | 63 | 100% | 652 ms | 2368 ms | 97.2 | 173.0 | 7.81 s | 12.68 s | 709 | $0.000530 |
| HAI | 63 | 98% | 3479 ms | 27568 ms | 100.2 | 235.0 | 9.42 s | 95.77 s | 546 | ¥0.1485 |

## Latest run

Run `20260927T135816Z-1680ee49` · `2026-09-27T13:58:16.171905+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36324222687)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1439 ms | 136.6 | 6.04 s | 279 | 628 | $0.000419 |
| DeepSeek | ok | stop | 988 ms | 224.0 | 4.40 s | 279 | 764 | $0.000500 |
| Fireworks | ok | stop | 1026 ms | 96.9 | 9.40 s | 279 | 811 | $0.000597 |
| HAI | ok | stop | 4010 ms | 100.1 | 8.57 s | 290 | 452 | ¥0.1259 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
