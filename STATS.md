# Benchmark statistics

Generated: `2026-09-24T22:24:37+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **49**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 49 | 100% | 1193 ms | 1871 ms | 234.3 | 262.5 | 4.38 s | 7.85 s | 710 | $0.000468 |
| DeepSeek | 49 | 100% | 868 ms | 1123 ms | 237.3 | 258.7 | 3.86 s | 4.63 s | 700 | $0.000477 |
| Fireworks | 49 | 100% | 642 ms | 2562 ms | 98.4 | 178.2 | 7.86 s | 11.02 s | 720 | $0.000536 |
| HAI | 49 | 98% | 3280 ms | 28758 ms | 99.8 | 223.2 | 8.80 s | 101.13 s | 544 | ¥0.1480 |

## Latest run

Run `20260924T222408Z-4a73f994` · `2026-09-24T22:24:08.676266+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36067190757)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1516 ms | 155.5 | 6.38 s | 280 | 756 | $0.000496 |
| DeepSeek | ok | stop | 565 ms | 234.5 | 3.69 s | 280 | 731 | $0.000481 |
| Fireworks | ok | stop | 497 ms | 114.9 | 7.01 s | 280 | 748 | $0.000555 |
| HAI | ok | stop | 4669 ms | 30.1 | 28.30 s | 291 | 708 | ¥0.1874 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
