# Benchmark statistics

Generated: `2026-10-08T21:19:55+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **112**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 112 | 100% | 1374 ms | 2623 ms | 180.2 | 250.8 | 5.29 s | 8.16 s | 704 | $0.000475 |
| DeepSeek | 112 | 100% | 833 ms | 1173 ms | 237.2 | 256.9 | 3.92 s | 4.85 s | 726 | $0.000486 |
| Fireworks | 112 | 100% | 704 ms | 2903 ms | 96.4 | 181.5 | 8.20 s | 13.90 s | 706 | $0.000528 |
| HAI | 112 | 97% | 3563 ms | 28015 ms | 95.8 | 197.6 | 10.40 s | 100.72 s | 573 | ¥0.1547 |

## Latest run

Run `20261008T211946Z-ad3c21fb` · `2026-10-08T21:19:46.776139+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37845963804)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1017 ms | 178.4 | 4.94 s | 282 | 699 | $0.000462 |
| DeepSeek | ok | stop | 547 ms | 242.8 | 3.22 s | 282 | 647 | $0.000431 |
| Fireworks | ok | stop | 1256 ms | 143.3 | 5.91 s | 282 | 666 | $0.000502 |
| HAI | ok | stop | 1916 ms | 111.2 | 8.16 s | 293 | 690 | ¥0.1832 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
