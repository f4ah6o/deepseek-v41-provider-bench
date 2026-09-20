# Benchmark statistics

Generated: `2026-09-20T01:09:07+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **22**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 22 | 100% | 1162 ms | 1489 ms | 239.6 | 266.7 | 4.13 s | 6.44 s | 689 | $0.000455 |
| DeepSeek | 22 | 100% | 941 ms | 1160 ms | 237.6 | 257.6 | 3.87 s | 4.87 s | 694 | $0.000476 |
| Fireworks | 22 | 100% | 713 ms | 2355 ms | 97.3 | 152.6 | 8.24 s | 11.17 s | 711 | $0.000530 |
| HAI | 22 | 95% | 2482 ms | 23137 ms | 100.2 | 237.0 | 7.33 s | 87.26 s | 541 | ¥0.1472 |

## Latest run

Run `20260920T010856Z-a12d8f93` · `2026-09-20T01:08:56.535310+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35480623774)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1463 ms | 246.5 | 3.87 s | 281 | 593 | $0.000398 |
| DeepSeek | ok | stop | 952 ms | 216.9 | 4.48 s | 281 | 764 | $0.000501 |
| Fireworks | ok | stop | 1472 ms | 71.5 | 10.76 s | 281 | 664 | $0.000500 |
| HAI | ok | stop | 1829 ms | 126.2 | 5.15 s | 292 | 418 | ¥0.1178 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
