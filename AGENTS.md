# AGENTS.md

Guidance for AI coding agents working in this repository.

## Project Overview

`python-starter` is a minimal, reusable Python project boilerplate.

- **Python**: 3.12+ (pinned via `.python-version`)
- **Package manager / env**: [uv](https://docs.astral.sh/uv/) — always use `uv`, never plain `pip` or manual venv management
- **Layout**: `src/`-based package at `src/python_starter/` (typed, PEP 561 `py.typed`)
- **Tooling**: pytest (with branch coverage), ruff (lint + format), mypy (strict), Docker multi-stage build, GitHub Actions CI

## Code Style

- Follow existing code conventions; do not introduce new style choices.
- Ruff is the single linter/formatter: `line-length = 100`, rules `E, F, I, UP, B`, Google-style docstrings.
- After making changes, run and fix:
  ```bash
  uv run ruff check .
  uv run ruff format .
  ```
- Keep code simple and dependency-free unless a runtime dependency is explicitly needed.

## Type Safety

- mypy runs in **strict** mode against `src/` (Python 3.12 target, `warn_unreachable`).
- All new code must be fully typed (annotations for parameters, returns, and non-trivial locals where inference is unclear).
- Do not delete or weaken `py.typed`, and do not disable type checkers with `# type: ignore` unless strictly required (with a reason comment).
- After changes: `uv run mypy src` must pass clean.

## Testing

- Tests live in `tests/` and use pytest; coverage is enforced on by default (`--cov=python_starter --cov-branch`).
- Write/update tests for any new behavior. Follow the patterns in `tests/test_hello.py` (plain asserts, fixtures, parametrization, `capsys` for CLI output).
- Run: `uv run pytest`

## Common Commands

```bash
uv sync                                   # install deps (uses uv.lock)
uv run python-starter --name pi           # run the CLI entry point
uv run pytest                             # tests + coverage
uv run ruff check . && uv run ruff format .
uv run mypy src
docker compose build                      # build image
docker compose run --rm --build app uv run --frozen -m pytest   # tests in container
```

## Dependencies

- Add with `uv add <pkg>` (runtime) or `uv add --group dev <pkg>` (dev) — this updates both `pyproject.toml` and `uv.lock`.
- Prefer the standard library; prefer existing dev tools over new ones.

## Definition of Done (CI parity)

Before considering any change complete, ensure all of the following pass locally (they mirror `.github/workflows/ci.yml`):

1. `uv run ruff check .`
2. `uv run ruff format --check .`
3. `uv run mypy src`
4. `uv run pytest`

## Repository Conventions

- Keep the project as a general template: avoid hardcoding project-specific names/values.
- Keep `README.md` in sync with any tooling, config, or workflow changes.
- Keep the entry point (`pyproject.toml` `[project.scripts]` → `python_starter.hello:main`) and the hatch packages config in `pyproject.toml` working if you move or rename modules.
