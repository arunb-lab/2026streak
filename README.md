# 2026streak

A personal learning / practice repository for Python exercises and small projects.

This repo is intentionally a collection of small scripts rather than a single installable package.

## Structure

- `basic_Python/` — small Python practice scripts (classes, loops, recursion, etc.)
- `project/` — project work (WIP)
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

Most scripts are standalone. If a script prints output immediately when run, that’s expected.

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
