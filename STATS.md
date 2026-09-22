# Benchmark statistics

Generated: `2026-09-22T09:58:09+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **35**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 35 | 100% | 1125 ms | 1614 ms | 238.1 | 266.6 | 4.19 s | 7.08 s | 710 | $0.000468 |
| DeepSeek | 35 | 100% | 906 ms | 1120 ms | 239.4 | 259.6 | 3.86 s | 4.66 s | 692 | $0.000477 |
| Fireworks | 35 | 100% | 688 ms | 1989 ms | 97.4 | 168.4 | 8.13 s | 10.89 s | 721 | $0.000537 |
| HAI | 35 | 97% | 3185 ms | 37261 ms | 97.6 | 211.5 | 8.18 s | 108.68 s | 522 | ¥0.1426 |

## Latest run

Run `20260922T095800Z-26d7f424` · `2026-09-22T09:58:00.749949+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35713320151)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 949 ms | 248.0 | 3.84 s | 282 | 716 | $0.000944 |
| DeepSeek | ok | stop | 651 ms | 260.4 | 2.44 s | 282 | 464 | $0.000641 |
| Fireworks | ok | stop | 988 ms | 173.5 | 5.29 s | 282 | 747 | $0.000555 |
| HAI | ok | stop | 2006 ms | 73.8 | 8.86 s | 293 | 502 | ¥0.1381 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
