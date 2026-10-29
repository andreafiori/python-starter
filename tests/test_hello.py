"""Example pytest tests for the boilerplate."""

import pytest

from python_starter import hello, main


def test_hello_default() -> None:
    assert hello() == "Hello, world!"


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("pi", "Hello, pi!"),
        ("uv", "Hello, uv!"),
    ],
)
def test_hello_custom_name(name: str, expected: str) -> None:
    assert hello(name) == expected


def test_main_prints_greeting(capsys: pytest.CaptureFixture[str]) -> None:
    main([])
    assert "Hello, world!" in capsys.readouterr().out


def test_main_with_name_flag(capsys: pytest.CaptureFixture[str]) -> None:
    main(["--name", "pi"])
    assert "Hello, pi!" in capsys.readouterr().out
