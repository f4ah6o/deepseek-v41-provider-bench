# Benchmark statistics

Generated: `2026-09-30T23:49:56+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **78**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 78 | 100% | 1332 ms | 2191 ms | 211.4 | 252.2 | 5.04 s | 8.01 s | 708 | $0.000469 |
| DeepSeek | 78 | 100% | 857 ms | 1141 ms | 236.9 | 256.3 | 3.86 s | 4.69 s | 718 | $0.000481 |
| Fireworks | 78 | 100% | 666 ms | 2398 ms | 96.7 | 169.3 | 8.03 s | 12.80 s | 712 | $0.000532 |
| HAI | 78 | 97% | 3404 ms | 27890 ms | 99.8 | 207.5 | 9.81 s | 97.87 s | 560 | ¥0.1520 |

## Latest run

Run `20260930T234926Z-360f1b72` · `2026-09-30T23:49:26.865570+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36793037947)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1296 ms | 184.9 | 5.25 s | 280 | 728 | $0.000479 |
| DeepSeek | ok | stop | 740 ms | 230.3 | 2.63 s | 280 | 434 | $0.000302 |
| Fireworks | ok | stop | 487 ms | 82.1 | 8.06 s | 280 | 622 | $0.000472 |
| HAI | ok | stop | 3322 ms | 21.3 | 29.01 s | 291 | 547 | ¥0.1487 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
