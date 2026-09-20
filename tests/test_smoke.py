from click.testing import CliRunner

from jsonl_check import __version__
from jsonl_check.cli import main


def test_version_is_available() -> None:
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert __version__ in result.output
