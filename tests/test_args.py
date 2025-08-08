import pytest
from src.lib.args import parse_args

def test_parse_args_defaults(mocker):
    """
    Tests that parse_args returns the correct default values when no arguments
    are provided.
    """
    mocker.patch("sys.argv", ["main.py"])
    args = parse_args()
    assert args.spec_url is None
    assert args.transport == "stdio"
    assert args.host == "127.0.0.1"
    assert args.port == 8000
    assert args.base_url == "http://localhost:9990"

def test_parse_args_custom(mocker):
    """
    Tests that parse_args correctly parses custom command-line arguments.
    """
    mocker.patch("sys.argv", [
        "main.py",
        "--spec-url", "http://example.com/spec.json",
        "--transport", "http",
        "--host", "0.0.0.0",
        "--port", "9000",
        "--base-url", "http://api.example.com"
    ])
    args = parse_args()
    assert args.spec_url == "http://example.com/spec.json"
    assert args.transport == "http"
    assert args.host == "0.0.0.0"
    assert args.port == 9000
    assert args.base_url == "http://api.example.com"

def test_parse_args_invalid_transport(mocker):
    """
    Tests that parse_args raises an error for an invalid transport choice.
    """
    mocker.patch("sys.argv", [
        "main.py",
        "--transport", "invalid"
    ])
    with pytest.raises(SystemExit):
        parse_args()
