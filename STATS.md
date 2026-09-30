# Benchmark statistics

Generated: `2026-09-30T19:20:25+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **77**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 77 | 100% | 1335 ms | 2213 ms | 216.5 | 252.5 | 5.04 s | 8.04 s | 705 | $0.000468 |
| DeepSeek | 77 | 100% | 868 ms | 1142 ms | 237.0 | 256.4 | 3.86 s | 4.69 s | 722 | $0.000482 |
| Fireworks | 77 | 100% | 677 ms | 2403 ms | 96.7 | 169.6 | 8.01 s | 12.80 s | 714 | $0.000533 |
| HAI | 77 | 97% | 3447 ms | 27908 ms | 100.1 | 209.5 | 9.78 s | 98.28 s | 565 | ¥0.1531 |

## Latest run

Run `20260930T191952Z-1832c893` · `2026-09-30T19:19:52.634220+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36764882842)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 2566 ms | 176.8 | 6.29 s | 282 | 657 | $0.000436 |
| DeepSeek | ok | stop | 683 ms | 245.5 | 3.86 s | 282 | 778 | $0.000509 |
| Fireworks | ok | stop | 1270 ms | 82.9 | 10.99 s | 282 | 806 | $0.000594 |
| HAI | ok | stop | 3610 ms | 22.1 | 32.29 s | 293 | 633 | ¥0.1695 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
