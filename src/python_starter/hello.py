"""Example module — replace with your own project code."""

import argparse


def hello(name: str = "world") -> str:
    """Return a greeting.

    Args:
        name: Name to greet.

    Returns:
        A greeting string.
    """
    return f"Hello, {name}!"


def main(argv: list[str] | None = None) -> None:
    """CLI entry point.

    Args:
        argv: Optional argument list (defaults to ``sys.argv[1:]``).
    """
    parser = argparse.ArgumentParser(
        prog="python-starter",
        description="Say hello to someone (example CLI — replace with your own).",
    )
    parser.add_argument(
        "--name",
        default="world",
        help="name to greet (default: %(default)s)",
    )
    args = parser.parse_args(argv)
    print(hello(args.name))


if __name__ == "__main__":
    main()
