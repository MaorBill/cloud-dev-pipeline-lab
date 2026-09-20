"""Command-line adapter for jsonl-check."""

import click

from jsonl_check import __version__


@click.command()
@click.version_option(version=__version__)
def main() -> None:
    """Validate newline-delimited JSON files.

    Validation behavior is introduced through the experiment Issues.
    """


if __name__ == "__main__":
    main()
