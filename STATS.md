# Benchmark statistics

Generated: `2026-09-22T00:08:46+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **33**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 33 | 100% | 1130 ms | 1655 ms | 238.1 | 266.7 | 4.23 s | 7.27 s | 710 | $0.000468 |
| DeepSeek | 33 | 100% | 906 ms | 1127 ms | 239.4 | 258.5 | 3.87 s | 4.69 s | 697 | $0.000477 |
| Fireworks | 33 | 100% | 688 ms | 2046 ms | 97.2 | 149.2 | 8.34 s | 10.94 s | 720 | $0.000536 |
| HAI | 33 | 97% | 3185 ms | 39543 ms | 99.8 | 215.4 | 7.60 s | 110.02 s | 532 | ¥0.1451 |

## Latest run

Run `20260922T000702Z-d2443796` · `2026-09-22T00:07:02.476446+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/35670555477)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 22724 ms | 133.8 | 27.79 s | 280 | 678 | $0.000449 |
| DeepSeek | ok | stop | 549 ms | 233.3 | 3.95 s | 280 | 793 | $0.000518 |
| Fireworks | ok | stop | 602 ms | 82.1 | 8.01 s | 280 | 608 | $0.000463 |
| HAI | ok | stop | 52096 ms | 15.7 | 103.98 s | 291 | 814 | ¥0.2128 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
