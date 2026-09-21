# Benchmark statistics

Generated: `2026-09-21T17:03:34+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **31**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 31 | 100% | 1125 ms | 1477 ms | 238.8 | 266.7 | 4.19 s | 5.94 s | 710 | $0.000468 |
| DeepSeek | 31 | 100% | 906 ms | 1133 ms | 239.9 | 258.6 | 3.86 s | 4.72 s | 692 | $0.000475 |
| Fireworks | 31 | 100% | 688 ms | 2102 ms | 97.4 | 149.8 | 8.34 s | 10.98 s | 720 | $0.000536 |
| HAI | 31 | 97% | 2889 ms | 28611 ms | 99.8 | 219.3 | 7.45 s | 107.12 s | 522 | ¥0.1426 |

## Latest run

Run `20260921T170328Z-c58fcc60` · `2026-09-21T17:03:28.236355+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35629523710)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1028 ms | 246.2 | 3.74 s | 279 | 667 | $0.000442 |
| DeepSeek | ok | stop | 1012 ms | 249.8 | 4.23 s | 279 | 802 | $0.000523 |
| Fireworks | ok | stop | 460 ms | 100.3 | 5.83 s | 279 | 539 | $0.000417 |
| HAI | ok | stop | 2349 ms | 128.9 | 5.46 s | 290 | 397 | ¥0.1127 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
