"""Command-line adapter for jsonl-check."""

from __future__ import annotations

from pathlib import Path

import click

from jsonl_check import __version__
from jsonl_check.reporting import render_text_report
from jsonl_check.validation import OperationalError, validate_jsonl


@click.command()
@click.argument(
    "path",
    required=False,
    type=click.Path(exists=False, dir_okay=False, path_type=Path),
)
@click.version_option(version=__version__)
def main(path: Path | None) -> None:
    """Validate newline-delimited JSON files."""
    if path is None:
        click.echo("error: missing PATH argument", err=True)
        raise SystemExit(2)

    try:
        result = validate_jsonl(path)
    except OperationalError as exc:
        click.echo(f"error: {exc}", err=True)
        raise SystemExit(2) from None

    click.echo(render_text_report(result), nl=False)
    if result.invalid:
        raise SystemExit(1)
    raise SystemExit(0)


if __name__ == "__main__":
    main()
