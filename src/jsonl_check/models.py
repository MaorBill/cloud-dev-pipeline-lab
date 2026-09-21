"""Typed validation results and diagnostics."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Diagnostic:
    """One invalid record with stable source coordinates."""

    path: str
    line: int
    message: str


@dataclass(frozen=True, slots=True)
class ValidationResult:
    """Aggregate outcome for one JSONL source file."""

    path: str
    records: int
    valid: int
    invalid: int
    diagnostics: tuple[Diagnostic, ...]
