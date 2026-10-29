# python-starter

A minimal, reusable Python project boilerplate built with [uv](https://docs.astral.sh/uv/),
`pytest`, and Docker.

## Layout

```text
├── .github/workflows/ci.yml  # lint, format, mypy, pytest, docker build
├── .python-version           # pins Python 3.12 for uv
├── Dockerfile                # multi-stage (build → slim runtime, tests excluded)
├── docker-compose.yml        # app service (+ commented examples for db, ports, ...)
├── pyproject.toml            # metadata, dev deps, tool config (pytest, ruff, mypy)
├── src/
│   └── python_starter/       # the package — rename for your project
│       ├── __init__.py
│       ├── hello.py          # example module with an argparse CLI entry point
│       └── py.typed          # marks the package as typed (PEP 561)
└── tests/
    └── test_hello.py         # example pytest tests (incl. parametrized & capsys)
```

## Prerequisites

- Python 3.12+
- uv: `pip install uv`
- Docker (for image builds)

## Quickstart

```bash
# Create the virtual environment and install deps (uses uv.lock)
uv sync

# Run the example CLI (supports --name)
uv run python-starter --name pi

# Run tests (coverage is on by default via pyproject addopts)
uv run pytest

# Lint / format check
uv run ruff check .
uv run ruff format .

# Type check
uv run mypy src

# Clear the venv
uv venv --clear
```

## Docker

```bash
# Build the image
docker compose build

# Run the app
docker compose up app --build

# Or run tests inside the image
docker compose run --rm --build app uv run --frozen -m pytest
```

## CI

`.github/workflows/ci.yml` runs on push/PR: `ruff check`, `ruff format --check`, `mypy`, `pytest` (with coverage), and a `docker compose build` smoke check.

## Turning it into a new project

1. Rename the package directory `src/python_starter/` to your project name (keep `py.typed` inside).
2. Update in `pyproject.toml`:
   - `project.name`, `description`
   - the `[project.scripts]` entry point
   - `[tool.hatch.build.targets.wheel].packages`
3. Rename `tests/` cases and the docker image name in `docker-compose.yml`.
4. Add runtime dependencies with `uv add <pkg>` (dev: `uv add --group dev <pkg>`).

## Adding dependencies

```bash
uv add requests            # runtime dependency
uv add --group dev httpx   # dev-only dependency
```

`uv add`/`uv remove` update both `pyproject.toml` and `uv.lock`.
