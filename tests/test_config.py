from pathlib import Path

from dsbench.config import load_config


def test_four_providers_are_configured():
    root = Path(__file__).resolve().parents[1]
    cfg = load_config(root / "benchmark.yaml")
    assert {p.name for p in cfg.providers} == {"opencode_go", "hai", "deepseek", "fireworks"}
    assert all(p.enabled for p in cfg.providers)
    assert cfg.profile.name == "repo-review"
    assert cfg.profile.max_output_tokens == 4096
