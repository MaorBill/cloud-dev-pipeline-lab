from __future__ import annotations

from pathlib import Path

import pytest

from jsonl_check.validation import OperationalError, validate_jsonl


def test_valid_three_line_file(tmp_path: Path) -> None:
    path = tmp_path / "sample.jsonl"
    path.write_text('{"a":1}\n{"b":2}\n{"c":3}\n', encoding="utf-8")

    result = validate_jsonl(path)

    assert result.records == 3
    assert result.valid == 3
    assert result.invalid == 0
    assert result.diagnostics == ()


def test_malformed_json_continues_and_reports_lines(tmp_path: Path) -> None:
    path = tmp_path / "broken.jsonl"
    path.write_text('{"ok": true}\nnot-json\n{"also": "ok"}\n', encoding="utf-8")

    result = validate_jsonl(path)

    assert result.records == 3
    assert result.valid == 2
    assert result.invalid == 1
    assert len(result.diagnostics) == 1
    diagnostic = result.diagnostics[0]
    assert diagnostic.path == str(path)
    assert diagnostic.line == 2
    assert diagnostic.message == "invalid JSON"


def test_blank_line_is_invalid(tmp_path: Path) -> None:
    path = tmp_path / "blank.jsonl"
    path.write_text('{"a":1}\n\n{"b":2}\n', encoding="utf-8")

    result = validate_jsonl(path)

    assert result.records == 3
    assert result.valid == 2
    assert result.invalid == 1
    assert result.diagnostics[0].line == 2
    assert result.diagnostics[0].message == "blank line"


def test_multiple_invalid_lines_are_ordered(tmp_path: Path) -> None:
    path = tmp_path / "many.jsonl"
    path.write_text("\n{}\n\n", encoding="utf-8")

    result = validate_jsonl(path)

    assert result.records == 3
    assert result.valid == 1
    assert result.invalid == 2
    assert [item.line for item in result.diagnostics] == [1, 3]
    assert [item.message for item in result.diagnostics] == ["blank line", "blank line"]


def test_missing_file_raises_operational_error(tmp_path: Path) -> None:
    path = tmp_path / "missing.jsonl"

    with pytest.raises(OperationalError, match="no such file"):
        validate_jsonl(path)


def test_directory_raises_operational_error(tmp_path: Path) -> None:
    with pytest.raises(OperationalError, match="not a file"):
        validate_jsonl(tmp_path)
