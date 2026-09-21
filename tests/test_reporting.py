from jsonl_check.models import Diagnostic, ValidationResult
from jsonl_check.reporting import render_text_report


def test_render_text_report_includes_summary_and_diagnostics() -> None:
    result = ValidationResult(
        path="/tmp/sample.jsonl",
        records=3,
        valid=2,
        invalid=1,
        diagnostics=(
            Diagnostic(path="/tmp/sample.jsonl", line=2, message="invalid JSON"),
        ),
    )

    rendered = render_text_report(result)

    assert rendered == (
        "records=3 valid=2 invalid=1\n"
        "/tmp/sample.jsonl:2: invalid JSON\n"
    )
