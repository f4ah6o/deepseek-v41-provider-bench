# Benchmark statistics

Generated: `2026-10-12T05:58:05+00:00`

Current profile: **`repo-review`** · max output: **4096 tokens** · runs: **127**

Raw compact history: [`data/history.csv`](data/history.csv). Raw responses/SSE remain in GitHub Actions artifacts.

## Provider summary

| Provider | Samples | Success | TTFT p50 | TTFT p95 | Decode p50 | Decode p95 | Wall p50 | Wall p95 | Output p50 | Cost p50 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | 127 | 91% | 1372 ms | 2597 ms | 178.0 | 250.5 | 5.29 s | 8.06 s | 704 | $0.000476 |
| DeepSeek | 127 | 100% | 847 ms | 1178 ms | 236.9 | 255.9 | 3.93 s | 4.92 s | 722 | $0.000484 |
| Fireworks | 127 | 100% | 720 ms | 3026 ms | 97.2 | 181.7 | 7.86 s | 13.62 s | 705 | $0.000527 |
| HAI | 127 | 98% | 3565 ms | 27102 ms | 95.8 | 197.3 | 11.32 s | 95.64 s | 573 | ¥0.1550 |

## Latest run

Run `20261012T055744Z-ca87ef17` · `2026-10-12T05:57:44.411312+00:00` · [GitHub Actions](https://github.com/f4ah6o/deepseek-v41-provider-bench/actions/runs/38210241470)

| Provider | Status | Finish | TTFT | Decode tok/s | Wall | Input | Output | Cost |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenCode Go | http_error | — | — | — | 0.34 s | — | — | — |
| DeepSeek | ok | stop | 685 ms | 194.8 | 3.99 s | 278 | 643 | $0.000427 |
| Fireworks | ok | stop | 2056 ms | 94.3 | 10.37 s | 278 | 784 | $0.000579 |
| HAI | ok | stop | 15173 ms | 95.9 | 20.99 s | 289 | 555 | ¥0.1505 |

## Notes

- p50 is the median. p95 uses linear interpolation over successful samples.
- TTFT and wall-time percentiles: lower is better. Decode tok/s: higher is better.
- Nominal cost is a token-rate comparison. Subscription providers are not charged per run by this table.
- With fewer than ~20 samples, p95 is descriptive rather than stable; hourly runs make it more useful over time.
- Statistics only combine samples with the same profile name, so the retired 512-token profile is not mixed into the current 4096-token summary.
