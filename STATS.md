# Benchmark statistics

Generated: `2026-10-04T02:39:47+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **93**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 93 | 100% | 1369 ms | 2357 ms | 189.8 | 250.7 | 5.23 s | 8.13 s | 703 | $0.000468 |
| DeepSeek | 93 | 100% | 831 ms | 1147 ms | 237.0 | 258.5 | 3.87 s | 4.84 s | 714 | $0.000480 |
| Fireworks | 93 | 100% | 698 ms | 2560 ms | 96.1 | 167.2 | 8.34 s | 13.34 s | 714 | $0.000533 |
| HAI | 93 | 97% | 3397 ms | 25702 ms | 100.1 | 197.7 | 9.85 s | 95.26 s | 560 | ¥0.1520 |

## Latest run

Run `20261004T023925Z-019bd94a` · `2026-10-04T02:39:25.774254+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/37171715154)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | ok | stop | 1833 ms | 192.4 | 5.32 s | 279 | 671 | $0.000444 |
| DeepSeek | ok | stop | 593 ms | 211.5 | 5.17 s | 279 | 968 | $0.000623 |
| Fireworks | ok | stop | 1206 ms | 65.2 | 13.32 s | 279 | 790 | $0.000583 |
| HAI | ok | stop | 3434 ms | 22.2 | 21.12 s | 290 | 392 | ¥0.1115 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
