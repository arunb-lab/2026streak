# 2026streak

![CI](https://github.com/arunb-lab/2026streak/actions/workflows/ci.yml/badge.svg)

A personal learning / practice repository for Python exercises and small projects.

This repo is intentionally a collection of small scripts rather than a single installable package.

## Structure

- `basic_Python/` — small Python practice scripts (classes, loops, recursion, etc.)
- `project/` — small "resume-ready" modules + mini-CLIs (typed + tested)
  - `project/date_range.py` — date range utilities (overlap, intersection, merge)
  - `project/date_range_cli.py` — tiny CLI to count days / business days
  - `project/api.py` — FastAPI mini-service exposing the same logic via HTTP
- `if-statement/` — practice snippets (WIP)
- `SnakeGame /` — game experiments (note: directory name contains a trailing space)
- `Dictonaries/` — notes/data (WIP)
- `file.py` — **NOT Python**. This appears to be Google Apps Script / JS-like code.

## Requirements

- Python 3.10+ recommended

## Run a script

From the repo root:

```bash
python basic_Python/area.py
```

## Run the DateRange CLI

```bash
python -m project.date_range_cli 2026-01-01..2026-01-31
python -m project.date_range_cli 2026-01-01..2026-01-31 --business-days
python -m project.date_range_cli 2026-01-01..2026-01-31 --split 7
python -m project.date_range_cli 2026-01-01..2026-01-31 --shift-days 1
```

## Run the FastAPI mini-service

Install requirements:

```bash
python -m pip install fastapi uvicorn httpx
```

Run locally:

```bash
uvicorn project.api:app --reload
```

Try it:

- Health: http://127.0.0.1:8000/health
- Docs (Swagger): http://127.0.0.1:8000/docs
- Example:
  - http://127.0.0.1:8000/daterange/info?range=2026-01-01..2026-01-31
  - http://127.0.0.1:8000/daterange/split?range=2026-01-01..2026-01-31&chunk_days=7

## Development (optional)

### Create a virtual environment

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows (PowerShell)
# .venv\Scripts\Activate.ps1
```

### Install dev tools

```bash
python -m pip install -U pip
python -m pip install pytest ruff
```

### Run tests

```bash
pytest
```

### Lint

```bash
ruff check .
```
