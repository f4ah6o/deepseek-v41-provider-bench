# Benchmark statistics

Generated: `2026-09-24T19:10:12+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **48**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 48 | 100% | 1188 ms | 1874 ms | 234.8 | 263.1 | 4.37 s | 7.86 s | 710 | $0.000468 |
| DeepSeek | 48 | 100% | 875 ms | 1125 ms | 237.3 | 258.8 | 3.87 s | 4.63 s | 698 | $0.000476 |
| Fireworks | 48 | 100% | 647 ms | 2577 ms | 97.9 | 178.5 | 7.93 s | 11.05 s | 713 | $0.000532 |
| HAI | 48 | 98% | 3113 ms | 28831 ms | 100.2 | 225.2 | 8.74 s | 101.54 s | 543 | ¥0.1476 |

## Latest run

Run `20260924T191002Z-6b847aa4` · `2026-09-24T19:10:02.859984+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36046251174)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1649 ms | 152.4 | 6.89 s | 280 | 799 | $0.000521 |
| DeepSeek | ok | stop | 845 ms | 225.5 | 3.97 s | 280 | 703 | $0.000464 |
| Fireworks | ok | stop | 1141 ms | 98.4 | 8.30 s | 280 | 705 | $0.000527 |
| HAI | ok | stop | 6478 ms | 245.9 | 9.06 s | 291 | 547 | ¥0.1487 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
