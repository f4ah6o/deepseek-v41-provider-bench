# Benchmark statistics

Generated: `2026-09-28T00:46:33+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **66**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 66 | 100% | 1263 ms | 2069 ms | 223.5 | 255.2 | 4.65 s | 7.71 s | 706 | $0.000468 |
| DeepSeek | 66 | 100% | 881 ms | 1156 ms | 237.1 | 257.4 | 3.86 s | 4.71 s | 718 | $0.000480 |
| Fireworks | 66 | 100% | 647 ms | 2344 ms | 97.0 | 172.3 | 7.64 s | 12.44 s | 706 | $0.000527 |
| HAI | 66 | 98% | 3360 ms | 26868 ms | 100.2 | 229.1 | 9.09 s | 95.58 s | 547 | ¥0.1487 |

## Latest run

Run `20260928T004624Z-f5b7ab0d` · `2026-09-28T00:46:24.271930+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/36363434105)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1851 ms | 126.6 | 7.67 s | 280 | 736 | $0.000484 |
| DeepSeek | ok | stop | 947 ms | 230.1 | 4.68 s | 280 | 854 | $0.000554 |
| Fireworks | ok | stop | 946 ms | 96.1 | 6.80 s | 280 | 562 | $0.000433 |
| HAI | ok | stop | 2080 ms | 85.0 | 9.09 s | 291 | 592 | ¥0.1595 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
