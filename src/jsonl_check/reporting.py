"""Pure rendering from validation result models."""

from jsonl_check.models import ValidationResult


def render_text_report(result: ValidationResult) -> str:
    """Render the default human-readable summary and diagnostics."""
    parts = [
        f"records={result.records} valid={result.valid} invalid={result.invalid}",
    ]
    parts.extend(f"{item.path}:{item.line}: {item.message}" for item in result.diagnostics)
    return "\n".join(parts) + "\n"
