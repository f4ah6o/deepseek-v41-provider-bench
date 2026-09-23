# Benchmark statistics

Generated: `2026-09-23T00:33:23+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **39**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 39 | 100% | 1130 ms | 1554 ms | 237.3 | 266.6 | 4.27 s | 6.69 s | 711 | $0.000476 |
| DeepSeek | 39 | 100% | 906 ms | 1108 ms | 239.4 | 259.4 | 3.80 s | 4.59 s | 689 | $0.000475 |
| Fireworks | 39 | 100% | 652 ms | 1877 ms | 99.1 | 181.7 | 7.86 s | 10.81 s | 702 | $0.000524 |
| HAI | 39 | 97% | 2889 ms | 32696 ms | 99.8 | 203.6 | 8.13 s | 105.99 s | 522 | ¥0.1426 |

## Latest run

Run `20260923T003314Z-11c97b57` · `2026-09-23T00:33:14.367544+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35802552699)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1199 ms | 223.0 | 4.45 s | 276 | 724 | $0.000476 |
| DeepSeek | ok | stop | 1001 ms | 242.6 | 2.69 s | 276 | 409 | $0.000287 |
| Fireworks | ok | stop | 275 ms | 181.3 | 3.62 s | 276 | 607 | $0.000461 |
| HAI | ok | stop | 3113 ms | 111.3 | 8.64 s | 287 | 615 | ¥0.1648 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
