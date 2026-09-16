# deepseek-v41-provider-bench

Reproducible benchmark for **DeepSeek V4.1 Flash** served by multiple providers. The initial provider set is OpenCode Go, HAI, DeepSeek Platform, and Fireworks AI.

The hourly benchmark sends the same prompt, context, output limit, and cache-busting nonce to all enabled providers concurrently. The default `repo-review` profile allows up to **4096 output tokens** so responses can complete naturally while still recording generation throughput. It records raw SSE chunks with timestamps, visible output, reasoning output when exposed, provider-reported token usage, TTFT, decode throughput, wall time, HTTP failures, and nominal token cost.

## Providers

| Provider | Model ID | Endpoint family | Billing note |
| --- | --- | --- | --- |
| OpenCode Go | `deepseek-v4.1-flash` | `https://opencode.ai/zen/go/v1/chat/completions` | subscription; nominal peak/off-peak rates retained for comparison |
| HAI | `deepseek-v4.1-flash` | `https://hai-api.hcloud.ltd/v1/chat/completions` | subscription; nominal JPY token rates retained |
| DeepSeek Platform | `deepseek-flash` | `https://api.deepseek.com/chat/completions` | prepaid; per-request guard enabled |
| Fireworks AI | `accounts/fireworks/models/deepseek-v4p1-flash` | `https://api.fireworks.ai/inference/v1/chat/completions` | prepaid; per-request guard enabled |

Provider-specific reasoning controls live in `benchmark.yaml`; this is intentional because the OpenAI-compatible surfaces are not perfectly identical.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
```

Set API keys without committing them:

```bash
export OPENCODE_GO_API_KEY=...
export HAI_API_KEY=...
export DEEPSEEK_API_KEY=...
export FIREWORKS_API_KEY=...
```

For GitHub Actions create repository secrets with those exact names.

## Run

Without a selected repository the deterministic fixture is used:

```bash
dsbench run
```

To benchmark a real repository, edit `repositories/manifest.yaml`, set exactly one entry to `selected: true`, and pin an exact 40-character commit SHA. Then:

```bash
dsbench prepare-context --output .cache/context.txt
dsbench run --context-file .cache/context.txt
dsbench aggregate
```

Results are written under `results/YYYY-MM-DD/<run-id>/`. Each provider gets `request.json`, `stream.jsonl`, `response.txt`, optional `reasoning.txt`, and `metrics.json`. API keys are never written to result files.

## Hourly GitHub Actions

`.github/workflows/hourly.yml` runs at minute 17 of every hour and can also be started manually. GitHub scheduled workflows are not guaranteed to begin at the exact cron minute; the actual start timestamp is therefore recorded in each run.

The workflow does not push generated benchmark data back to the repository. It uploads the `results/` directory as a 30-day Actions artifact, avoiding hourly commit noise and accidental persistence of model output on the public branch.

## Fairness controls

- Requests are launched concurrently with `asyncio.gather`.
- The same prompt/context and 4096-token output cap are used for every provider in a run.
- A random nonce is prepended to each hourly prompt to make the default profile a cold-prefix measurement.
- Provider-reported usage is used for tok/s. If a provider omits streaming usage, `decode_tok_sec` remains null rather than inventing a tokenizer estimate.
- OpenCode Go gets a benchmark-specific User-Agent and stable `x-opencode-session` for the conversation.
- DeepSeek Platform and Fireworks have a conservative maximum estimated per-request cost guard in `benchmark.yaml`.
- Peak/off-peak pricing is calculated using UTC and weekday rules from the provider pricing config.

## Candidate repositories

The initial candidate set is recorded but intentionally unselected:

- `f4ah6o/direct-go-sdk`
- `f4ah6o/temote-mcp`
- `opz-rs/opz` (candidate originally referred to as `f4ah6o/opz`)
- `f4ah6o/calver-action`
- `f4ah6o/Proped`
- `horideicom/jww_parser.mbt`

Selection and commit pinning are kept separate from the harness implementation so benchmark inputs cannot silently drift with default branches.

## Cost guard scope

`max_estimated_request_cost` is a **per-request** guard, not a live account-balance query. `balance_hint: 5.0` documents the initial prepaid amount for DeepSeek Platform and Fireworks but is not treated as authoritative balance state. Account consoles remain the source of truth for remaining credit.
