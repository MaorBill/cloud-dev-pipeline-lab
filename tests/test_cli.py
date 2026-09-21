from __future__ import annotations

from pathlib import Path

from click.testing import CliRunner

from jsonl_check import __version__
from jsonl_check.cli import main


def test_version_is_available() -> None:
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert __version__ in result.output


def test_valid_file_exits_zero(tmp_path: Path) -> None:
    path = tmp_path / "good.jsonl"
    path.write_text('{"x":1}\n{"y":2}\n{"z":3}\n', encoding="utf-8")

    result = CliRunner().invoke(main, [str(path)])

    assert result.exit_code == 0
    assert result.output == "records=3 valid=3 invalid=0\n"


def test_invalid_file_exits_one_with_diagnostics(tmp_path: Path) -> None:
    path = tmp_path / "bad.jsonl"
    path.write_text('{"ok": true}\n\n', encoding="utf-8")

    result = CliRunner().invoke(main, [str(path)])

    assert result.exit_code == 1
    assert result.output == (
        f"records=2 valid=1 invalid=1\n{path}:2: blank line\n"
    )


def test_missing_file_exits_two_without_traceback(tmp_path: Path) -> None:
    path = tmp_path / "missing.jsonl"

    result = CliRunner().invoke(main, [str(path)])

    assert result.exit_code == 2
    combined = result.output + result.stderr
    assert f"error: no such file: {path}" in combined
    assert "Traceback" not in combined


def test_missing_path_argument_exits_two() -> None:
    result = CliRunner().invoke(main, [])

    assert result.exit_code == 2
    assert "error: missing PATH argument" in result.output + result.stderr
