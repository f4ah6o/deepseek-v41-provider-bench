# Benchmark statistics

Generated: `2026-10-02T20:45:08+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **86**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 86 | 100% | 1336 ms | 2455 ms | 192.8 | 251.2 | 5.18 s | 8.30 s | 708 | $0.000472 |
| DeepSeek | 86 | 100% | 857 ms | 1156 ms | 237.1 | 256.0 | 3.90 s | 4.79 s | 720 | $0.000481 |
| Fireworks | 86 | 100% | 685 ms | 2631 ms | 96.6 | 168.0 | 8.20 s | 12.97 s | 720 | $0.000537 |
| HAI | 86 | 97% | 3322 ms | 27335 ms | 100.2 | 197.7 | 9.78 s | 95.71 s | 565 | ¥0.1531 |

## Latest run

Run `20261002T204445Z-d3b1f9c4` · `2026-10-02T20:44:45.185253+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37062518664)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1947 ms | 189.8 | 6.62 s | 277 | 887 | $0.000574 |
| DeepSeek | ok | stop | 665 ms | 246.4 | 3.90 s | 277 | 797 | $0.000520 |
| Fireworks | ok | stop | 14666 ms | 117.4 | 23.30 s | 277 | 1014 | $0.000730 |
| HAI | ok | stop | 2229 ms | 106.9 | 6.09 s | 288 | 410 | ¥0.1157 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
