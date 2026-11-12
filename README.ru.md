# thyra

[![CI](https://github.com/SajKey/thyra/actions/workflows/ci.yml/badge.svg)](https://github.com/SajKey/thyra/actions/workflows/ci.yml)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![uv](https://img.shields.io/badge/managed%20by-uv-de5fe9)](https://docs.astral.sh/uv/)
[![Ruff](https://img.shields.io/badge/lint%20%2B%20format-ruff-261230)](https://docs.astral.sh/ruff/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

[English](README.md) · **Русский**

Минимальный скелет Python-сервиса. Окружение, линтеры и хуки на коммит уже
настроены — первое, что ты пишешь, это рабочий код, а не конфиги.

> If the doors of perception were cleansed every thing would appear to man as
> it is, infinite.
>
> — Уильям Блейк, «Бракосочетание неба и ада» (1790–1793)

## Что внутри

- **uv** — окружение и зависимости, `venv` руками не нужен
- **ruff** — линтер и форматтер в одном инструменте, вместо black + isort + flake8
- **pre-commit** — на каждом коммите исправляет и проверяет код
- **`app/config.py`** — валидация `.env`, падение при старте, если чего-то нет
- **`app/logger.py`** — loguru, настроенный в одном месте
- **`main.py`** — тонкая точка входа, только сборка

## Структура

```
.
├── app/
│   ├── __init__.py
│   ├── config.py        # разбор env, fail-fast
│   └── logger.py        # setup_logging()
├── tests/
│   └── test_config.py
├── main.py              # точка входа
├── .env.example         # копируется в .env
├── .pre-commit-config.yaml
├── pyproject.toml       # зависимости + конфиг ruff и pytest
└── uv.lock
```

## Быстрый старт

```bash
uv sync                     # создать .venv и поставить зависимости
cp .env.example .env        # заполнить своими значениями
uv run pre-commit install   # включить хук на коммит
uv run python main.py
```

## Команды

| Команда | Что делает |
|---|---|
| `uv sync` | создать `.venv` и поставить всё из `uv.lock` |
| `uv run python main.py` | запустить приложение |
| `uv run pytest -q` | прогнать тесты |
| `uv run ruff check --fix .` | линт с автоисправлением |
| `uv run ruff format .` | форматирование |
| `uv run pre-commit run --all-files` | прогнать все хуки на всех файлах |

## Переменные окружения

`.env` в `.gitignore`, в git лежит только `.env.example`.

| Переменная | Обязательна | По умолчанию | Смысл |
|---|---|---|---|
| `DATABASE_URL` | да | — | строка подключения к БД |
| `SECRET_KEY` | да | — | секрет для подписи, токенов, сессий |
| `DEBUG` | нет | `false` | подробное поведение |
| `LOG_LEVEL` | нет | `INFO` | уровень логирования |

Если обязательной переменной нет, приложение падает сразу на старте, а не
посреди запроса.

## Как использовать как шаблон

Кнопка **Use this template** на GitHub, или:

```bash
gh repo create my-project --template SajKey/thyra --private --clone
cd my-project
uv sync && uv run pre-commit install && cp .env.example .env
```

Дальше поправь `name` в `pyproject.toml` и перепиши этот README.

## Лицензия

MIT. Лицензия относится к самому шаблону — проекты, созданные из него,
должны нести свою.
