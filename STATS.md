# Benchmark statistics

Generated: `2026-09-21T05:04:56+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **29**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 29 | 100% | 1137 ms | 1480 ms | 238.1 | 266.7 | 4.23 s | 6.05 s | 710 | $0.000468 |
| DeepSeek | 29 | 100% | 906 ms | 1139 ms | 239.4 | 258.7 | 3.86 s | 4.76 s | 692 | $0.000475 |
| Fireworks | 29 | 100% | 688 ms | 2158 ms | 97.4 | 150.4 | 8.34 s | 11.02 s | 720 | $0.000536 |
| HAI | 29 | 97% | 3185 ms | 28758 ms | 97.6 | 223.2 | 7.60 s | 109.40 s | 522 | ¥0.1426 |

## Latest run

Run `20260921T050446Z-2ff4a3b2` · `2026-09-21T05:04:46.651592+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35563208706)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 803 ms | 225.2 | 5.13 s | 281 | 974 | $0.000627 |
| DeepSeek | ok | stop | 1035 ms | 262.7 | 3.56 s | 281 | 660 | $0.000438 |
| Fireworks | ok | stop | 532 ms | 96.1 | 9.32 s | 281 | 844 | $0.000619 |
| HAI | ok | stop | 2923 ms | 122.3 | 6.49 s | 292 | 436 | ¥0.1222 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
