from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
import os
import yaml


@dataclass(frozen=True)
class Profile:
    name: str
    prompt_file: Path
    fallback_context_file: Path
    max_output_tokens: int
    timeout_seconds: float
    user_agent: str
    cold_cache_nonce: bool = True


@dataclass(frozen=True)
class Provider:
    name: str
    enabled: bool
    base_url: str
    model: str
    api_key_env: str
    billing_mode: str
    request_overrides: dict[str, Any] = field(default_factory=dict)
    headers: dict[str, str] = field(default_factory=dict)
    pricing: dict[str, Any] = field(default_factory=dict)
    balance_hint: float | None = None
    max_estimated_request_cost: float | None = None

    @property
    def api_key(self) -> str | None:
        return os.getenv(self.api_key_env)


@dataclass(frozen=True)
class Config:
    root: Path
    schema_version: int
    profile: Profile
    providers: tuple[Provider, ...]


def load_config(path: str | Path) -> Config:
    path = Path(path).resolve()
    root = path.parent
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    p = raw["profile"]
    profile = Profile(
        name=str(p["name"]),
        prompt_file=root / p["prompt_file"],
        fallback_context_file=root / p["fallback_context_file"],
        max_output_tokens=int(p["max_output_tokens"]),
        timeout_seconds=float(p["timeout_seconds"]),
        user_agent=str(p["user_agent"]),
        cold_cache_nonce=bool(p.get("cold_cache_nonce", True)),
    )
    providers = tuple(
        Provider(
            name=name,
            enabled=bool(v.get("enabled", False)),
            base_url=str(v["base_url"]).rstrip("/"),
            model=str(v["model"]),
            api_key_env=str(v["api_key_env"]),
            billing_mode=str(v.get("billing_mode", "unknown")),
            request_overrides=dict(v.get("request_overrides") or {}),
            headers=dict(v.get("headers") or {}),
            pricing=dict(v.get("pricing") or {}),
            balance_hint=float(v["balance_hint"]) if v.get("balance_hint") is not None else None,
            max_estimated_request_cost=(float(v["max_estimated_request_cost"]) if v.get("max_estimated_request_cost") is not None else None),
        )
        for name, v in raw["providers"].items()
    )
    return Config(root=root, schema_version=int(raw["schema_version"]), profile=profile, providers=providers)
