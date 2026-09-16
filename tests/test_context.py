from pathlib import Path

from dsbench.context import build_context


def test_context_is_deterministic_and_skips_lockfile(tmp_path: Path):
    (tmp_path / "README.md").write_text("hello", encoding="utf-8")
    (tmp_path / "a.py").write_text("print('x')", encoding="utf-8")
    (tmp_path / "package-lock.json").write_text("noise", encoding="utf-8")
    a = build_context(tmp_path)
    b = build_context(tmp_path)
    assert a == b
    assert "README.md" in a
    assert "a.py" in a
    assert "package-lock.json" not in a


def test_context_skips_oversized_chunk_and_keeps_later_file(tmp_path: Path):
    (tmp_path / "README.md").write_text("x" * 200, encoding="utf-8")
    (tmp_path / "a.py").write_text("ok = True", encoding="utf-8")
    context = build_context(tmp_path, max_context_bytes=100, max_file_bytes=1000)
    assert "a.py" in context
    assert "README.md" not in context
