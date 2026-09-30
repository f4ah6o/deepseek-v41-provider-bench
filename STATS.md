# Benchmark statistics

Generated: `2026-09-30T06:45:26+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **75**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 75 | 100% | 1330 ms | 1972 ms | 218.3 | 253.0 | 4.99 s | 8.09 s | 705 | $0.000468 |
| DeepSeek | 75 | 100% | 881 ms | 1144 ms | 237.0 | 256.6 | 3.86 s | 4.70 s | 714 | $0.000481 |
| Fireworks | 75 | 100% | 656 ms | 2412 ms | 96.9 | 170.1 | 7.86 s | 12.81 s | 709 | $0.000530 |
| HAI | 75 | 97% | 3360 ms | 27944 ms | 100.2 | 213.4 | 9.16 s | 99.09 s | 556 | ¥0.1509 |

## Latest run

Run `20260930T064320Z-c5a378db` · `2026-09-30T06:43:20.562427+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36679686527)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1139 ms | 220.3 | 5.74 s | 278 | 1013 | $0.001299 |
| DeepSeek | ok | stop | 757 ms | 249.4 | 3.07 s | 278 | 577 | $0.000776 |
| Fireworks | ok | stop | 1238 ms | 102.3 | 8.89 s | 278 | 783 | $0.000578 |
| HAI | ok | stop | 28157 ms | 6.4 | 125.78 s | 289 | 621 | ¥0.1664 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
