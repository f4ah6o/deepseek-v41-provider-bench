from __future__ import annotations

import argparse
import asyncio
from datetime import datetime, timezone
import json
from pathlib import Path
import uuid

from .aggregate import aggregate
from .config import load_config
from .context import build_context, checkout_public_repo, selected_repositories
from .provider import RunInput, run_provider


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="dsbench")
    sub = p.add_subparsers(dest="command", required=True)

    run = sub.add_parser("run", help="run enabled providers concurrently")
    run.add_argument("--config", default="benchmark.yaml")
    run.add_argument("--context-file")
    run.add_argument("--results-dir", default="results")
    run.add_argument("--providers", help="comma-separated subset")

    ctx = sub.add_parser("prepare-context", help="build deterministic context from one selected pinned public repository")
    ctx.add_argument("--manifest", default="repositories/manifest.yaml")
    ctx.add_argument("--cache-dir", default=".cache/repos")
    ctx.add_argument("--output", default=".cache/context.txt")
    ctx.add_argument("--max-context-bytes", type=int, default=120_000)
    ctx.add_argument("--max-file-bytes", type=int, default=30_000)

    agg = sub.add_parser("aggregate", help="aggregate metrics.json files into CSV")
    agg.add_argument("--results-dir", default="results")
    agg.add_argument("--output", default="results/hourly.csv")
    return p


def main() -> None:
    args = parser().parse_args()
    if args.command == "run":
        asyncio.run(_run(args))
    elif args.command == "prepare-context":
        _prepare_context(args)
    elif args.command == "aggregate":
        count = aggregate(Path(args.results_dir), Path(args.output))
        print(json.dumps({"rows": count, "output": args.output}))


async def _run(args: argparse.Namespace) -> None:
    cfg = load_config(args.config)
    prompt = cfg.profile.prompt_file.read_text(encoding="utf-8")
    context_path = Path(args.context_file) if args.context_file else cfg.profile.fallback_context_file
    context = context_path.read_text(encoding="utf-8")

    now = datetime.now(timezone.utc)
    run_id = now.strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:8]
    session_id = f"dsbench-{run_id}"
    nonce = str(uuid.uuid4()) if cfg.profile.cold_cache_nonce else None
    run_input = RunInput(run_id=run_id, session_id=session_id, prompt=prompt, context=context, nonce=nonce)
    out_dir = Path(args.results_dir) / now.strftime("%Y-%m-%d") / run_id
    out_dir.mkdir(parents=True, exist_ok=True)

    requested = set(args.providers.split(",")) if args.providers else None
    providers = [p for p in cfg.providers if p.enabled and (requested is None or p.name in requested)]
    if not providers:
        raise SystemExit("no enabled providers selected")

    meta = {
        "schema_version": 1,
        "run_id": run_id,
        "scheduled_at": now.isoformat(),
        "profile": cfg.profile.name,
        "context_file": str(context_path),
        "providers": [p.name for p in providers],
        "cold_cache_nonce": bool(nonce),
    }
    (out_dir / "run.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    results = await asyncio.gather(*(run_provider(p, cfg.profile, run_input, out_dir) for p in providers))
    print(json.dumps(results, ensure_ascii=False, indent=2))


def _prepare_context(args: argparse.Namespace) -> None:
    manifest = Path(args.manifest)
    repos = selected_repositories(manifest)
    if len(repos) != 1:
        raise SystemExit(f"prepare-context currently requires exactly one selected repo; found {len(repos)}")
    spec = repos[0]
    repo_dir = checkout_public_repo(spec["repository"], spec["commit"], Path(args.cache_dir))
    context = build_context(repo_dir, max_context_bytes=args.max_context_bytes, max_file_bytes=args.max_file_bytes)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(context, encoding="utf-8")
    print(json.dumps({"repository": spec["repository"], "commit": spec["commit"], "bytes": len(context.encode()), "output": str(output)}))


if __name__ == "__main__":
    main()
