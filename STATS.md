# Benchmark statistics

Generated: `2026-09-18T04:44:21+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **10**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 10 | 100% | 1135 ms | 1716 ms | 236.8 | 267.1 | 3.97 s | 6.68 s | 660 | $0.000438 |
| DeepSeek | 10 | 100% | 953 ms | 1177 ms | 237.4 | 249.9 | 4.10 s | 4.74 s | 710 | $0.000476 |
| Fireworks | 10 | 100% | 689 ms | 1867 ms | 97.3 | 168.0 | 7.87 s | 9.76 s | 700 | $0.000523 |
| HAI | 10 | 100% | 2644 ms | 15667 ms | 97.6 | 139.8 | 8.18 s | 70.33 s | 532 | ¥0.1449 |

## Latest run

Run `20260918T044342Z-a641e9ca` · `2026-09-18T04:43:42.464488+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35308046595)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 931 ms | 266.6 | 3.42 s | 279 | 633 | $0.000422 |
| DeepSeek | ok | stop | 961 ms | 240.0 | 4.56 s | 279 | 859 | $0.000557 |
| Fireworks | ok | stop | 689 ms | 97.2 | 7.62 s | 279 | 670 | $0.000504 |
| HAI | ok | stop | 4579 ms | 15.5 | 38.26 s | 290 | 520 | ¥0.1422 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
