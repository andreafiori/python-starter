# syntax=docker/dockerfile:1

FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Install uv first to leverage its caching layer
RUN pip install uv

# Run as non-root user for all package/venv operations
RUN useradd --create-home appuser && chown appuser:appuser /app
USER appuser

# ---- Build stage: sync dependencies, keep tests out of the final image ----
FROM base AS builder

# Bring in project metadata, lockfile and package code
COPY pyproject.toml uv.lock README.md ./
COPY src ./src
COPY tests ./tests

# Sync deps from the lockfile and install the project itself
RUN uv sync --frozen --no-dev

# ---- Final stage: runtime only (no tests/) ----
FROM base

# NOTE: absolute paths are kept identical to the builder stage so the
# editable install and entry points inside .venv keep working.
COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/src /app/src
COPY --from=builder /app/pyproject.toml /app/pyproject.toml
COPY --from=builder /app/uv.lock /app/uv.lock

# Make the venv's entry points available on PATH
ENV PATH="/app/.venv/bin:$PATH"

CMD ["python-starter"]
