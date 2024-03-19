import pytest
from src import parser


def test_pyrat_args(capsys):
    parser.add_argument("--new_arg", default="default", help="introduce new args")

    # Parse args in helper mode. New argument(s) should be printed
    with pytest.raises(SystemExit):
        args, _ = parser.parse_known_args(["-h"])

    captured = capsys.readouterr()
    assert "introduce new args" in captured.out

    # Parse args to verify content of new_arg
    args = parser.parse_args(["--new_arg", "new_value"])
    assert args.new_arg == "new_value"
