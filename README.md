# thyra

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![uv](https://img.shields.io/badge/managed%20by-uv-de5fe9)](https://docs.astral.sh/uv/)
[![Ruff](https://img.shields.io/badge/lint%20%2B%20format-ruff-261230)](https://docs.astral.sh/ruff/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**English** · [Русский](README.ru.md)

A minimal Python service skeleton. The environment, linting and commit hooks
are already wired — the first thing you write is actual code.

> If the doors of perception were cleansed every thing would appear to man as
> it is, infinite.
>
> — William Blake, *The Marriage of Heaven and Hell* (1790–1793)

## What's inside

- **uv** — environment and dependencies, no manual `venv`
- **ruff** — lint + format in one tool instead of black, isort and flake8
- **pre-commit** — fixes and checks the code on every commit
- **`app/config.py`** — `.env` validation that fails fast on startup
- **`app/logger.py`** — loguru configured in one place
- **`main.py`** — thin entrypoint, wiring only

## Layout

```
.
├── app/
│   ├── __init__.py
│   ├── config.py        # env parsing, fail-fast
│   └── logger.py        # setup_logging()
├── tests/
│   └── test_config.py
├── main.py              # entrypoint
├── .env.example         # copy to .env
├── .pre-commit-config.yaml
├── pyproject.toml       # deps + ruff + pytest config
└── uv.lock
```

## Quick start

```bash
uv sync                     # create .venv, install deps
cp .env.example .env        # fill in your values
uv run pre-commit install   # enable the commit hook
uv run python main.py
```

## Commands

| Command | Does |
|---|---|
| `uv sync` | create `.venv` and install from `uv.lock` |
| `uv run python main.py` | run the app |
| `uv run pytest -q` | run tests |
| `uv run ruff check --fix .` | lint and autofix |
| `uv run ruff format .` | format |
| `uv run pre-commit run --all-files` | run every hook on every file |

## Configuration

`.env` is git-ignored; `.env.example` is the template and lives in git.

| Variable | Required | Default | Meaning |
|---|---|---|---|
| `DATABASE_URL` | yes | — | database connection string |
| `SECRET_KEY` | yes | — | secret for signing, tokens, sessions |
| `DEBUG` | no | `false` | verbose behaviour |
| `LOG_LEVEL` | no | `INFO` | loguru level |

Missing required variables make the app fail immediately on startup instead
of failing halfway through a request.

## Use as a template

Click **Use this template** on GitHub, or:

```bash
gh repo create my-project --template SajKey/thyra --private --clone
cd my-project
uv sync && uv run pre-commit install && cp .env.example .env
```

Then rename `name` in `pyproject.toml` and rewrite this README.

## License

MIT. The license applies to the template itself — generated projects should
carry their own.
