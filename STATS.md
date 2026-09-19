# Benchmark statistics

Generated: `2026-09-19T05:53:19+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **16**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 16 | 100% | 1141 ms | 1593 ms | 236.8 | 266.9 | 4.13 s | 6.98 s | 689 | $0.000455 |
| DeepSeek | 16 | 100% | 953 ms | 1169 ms | 237.4 | 253.8 | 3.93 s | 5.06 s | 694 | $0.000476 |
| Fireworks | 16 | 100% | 688 ms | 3217 ms | 98.3 | 161.0 | 7.87 s | 11.74 s | 720 | $0.000537 |
| HAI | 16 | 94% | 2854 ms | 24978 ms | 95.6 | 168.8 | 8.74 s | 89.45 s | 545 | ¥0.1483 |

## Latest run

Run `20260919T055305Z-a8dbd104` · `2026-09-19T05:53:05.649376+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35425123110)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1137 ms | 242.2 | 4.27 s | 278 | 755 | $0.000495 |
| DeepSeek | ok | stop | 991 ms | 233.9 | 3.40 s | 278 | 561 | $0.000378 |
| Fireworks | ok | stop | 5717 ms | 99.1 | 13.39 s | 278 | 760 | $0.000563 |
| HAI | ok | stop | 2329 ms | 197.7 | 6.41 s | 289 | 786 | ¥0.2060 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
