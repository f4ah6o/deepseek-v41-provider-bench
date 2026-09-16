from __future__ import annotations

from pathlib import Path
from typing import Iterable
import subprocess
import yaml

TEXT_SUFFIXES = {
    ".c", ".cc", ".cpp", ".css", ".go", ".h", ".hpp", ".html", ".java", ".js", ".json",
    ".jsx", ".md", ".mbt", ".py", ".rs", ".sh", ".toml", ".ts", ".tsx", ".txt", ".yaml", ".yml",
}
SKIP_NAMES = {"package-lock.json", "pnpm-lock.yaml", "yarn.lock", "Cargo.lock"}


def selected_repositories(manifest_path: Path) -> list[dict]:
    raw = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    selected = [r for r in raw.get("repositories", []) if r.get("selected")]
    for repo in selected:
        sha = repo.get("commit")
        if not isinstance(sha, str) or len(sha) != 40:
            raise ValueError(f"selected repository {repo['repository']} must pin a 40-char commit SHA")
    return selected


def checkout_public_repo(repository: str, commit: str, cache_root: Path) -> Path:
    slug = repository.replace("/", "__")
    dest = cache_root / slug / commit
    if (dest / ".git").exists():
        return dest
    dest.mkdir(parents=True, exist_ok=True)
    _git(["init", "-q"], dest)
    _git(["remote", "add", "origin", f"https://github.com/{repository}.git"], dest)
    _git(["fetch", "--depth", "1", "origin", commit], dest)
    _git(["checkout", "--detach", "FETCH_HEAD"], dest)
    return dest


def build_context(repo_dir: Path, *, max_context_bytes: int = 120_000, max_file_bytes: int = 30_000) -> str:
    chunks: list[str] = []
    used = 0
    for path in _candidate_files(repo_dir):
        rel = path.relative_to(repo_dir).as_posix()
        if path.name in SKIP_NAMES or path.stat().st_size > max_file_bytes:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        chunk = f"FILE: {rel}\n```\n{text}\n```\n"
        encoded = chunk.encode("utf-8")
        if used + len(encoded) > max_context_bytes:
            continue
        chunks.append(chunk)
        used += len(encoded)
    if not chunks:
        raise ValueError(f"no suitable text files found in {repo_dir}")
    return "\n".join(chunks)


def _candidate_files(root: Path) -> Iterable[Path]:
    preferred_names = {"README.md", "pyproject.toml", "Cargo.toml", "go.mod", "package.json", "moon.mod.json"}
    files = [
        p for p in root.rglob("*")
        if p.is_file() and ".git" not in p.parts
        and (p.suffix.lower() in TEXT_SUFFIXES or p.name in preferred_names)
    ]
    return iter(sorted(files, key=lambda p: (0 if p.name in preferred_names else 1, p.relative_to(root).as_posix())))


def _git(args: list[str], cwd: Path) -> None:
    subprocess.run(["git", *args], cwd=cwd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
