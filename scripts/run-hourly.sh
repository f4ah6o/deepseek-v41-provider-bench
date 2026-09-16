#!/usr/bin/env bash
set -euo pipefail

CONTEXT_ARGS=()
if python -m dsbench.cli prepare-context --output .cache/context.txt; then
  CONTEXT_ARGS=(--context-file .cache/context.txt)
else
  echo "No single pinned repository selected; using deterministic fallback fixture." >&2
fi
python -m dsbench.cli run "${CONTEXT_ARGS[@]}"
python -m dsbench.cli aggregate
