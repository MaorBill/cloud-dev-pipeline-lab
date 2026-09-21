"""JSONL parsing and validation without console I/O."""

from __future__ import annotations

import json
from pathlib import Path

from jsonl_check.models import Diagnostic, ValidationResult


class OperationalError(Exception):
    """Input could not be read or validated as a file."""


def validate_jsonl(path: Path) -> ValidationResult:
    """Validate one UTF-8 JSONL file, one physical line per record."""
    if not path.exists():
        msg = f"no such file: {path}"
        raise OperationalError(msg)
    if not path.is_file():
        msg = f"not a file: {path}"
        raise OperationalError(msg)

    try:
        content = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise OperationalError(str(exc)) from exc
    except UnicodeDecodeError as exc:
        raise OperationalError(str(exc)) from exc

    source = str(path)
    lines = content.splitlines()
    diagnostics: list[Diagnostic] = []
    valid = 0

    for line_number, line in enumerate(lines, start=1):
        if line == "":
            diagnostics.append(
                Diagnostic(path=source, line=line_number, message="blank line")
            )
            continue
        try:
            json.loads(line)
        except json.JSONDecodeError:
            diagnostics.append(
                Diagnostic(path=source, line=line_number, message="invalid JSON")
            )
        else:
            valid += 1

    records = len(lines)
    invalid = records - valid
    return ValidationResult(
        path=source,
        records=records,
        valid=valid,
        invalid=invalid,
        diagnostics=tuple(diagnostics),
    )
