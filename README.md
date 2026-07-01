# pyforge

A forge for Python projects — a curated collection of small, typed, tested Python services, tools, and algorithms.

![Python](https://img.shields.io/badge/python-3.10%2B-blue) ![License: MIT](https://img.shields.io/badge/license-MIT-green) ![Lint: ruff](https://img.shields.io/badge/lint-ruff-orange)

`pyforge` is a mono-repo of self-contained Python projects. Everything here is meant to be readable, deterministic, and covered by tests — from a production-leaning FastAPI service to interview-ready DSA implementations.

## Highlights

- **FastAPI service** — an app-factory microservice with typed models, health/version endpoints, and pytest + httpx tests.
- **DateRange toolkit** — date-range utilities (overlap, intersection, merge, business days) with a CLI and an HTTP API.
- **Contribution heatmap** — a zero-dependency generator that renders a GitHub-style contribution grid as SVG.
- **DSA** — clean, typed, test-backed data structures and algorithms for interview prep.

## Repository layout

```text
pyforge/
├── src/
│   ├── fastapi_service/   # production-leaning FastAPI microservice
│   ├── daterange/         # date-range utilities + CLI + API
│   └── heatmap/           # SVG contribution-heatmap generator
├── dsa/                   # data structures & algorithms (typed + tested)
├── learning/              # beginner practice scripts (kept for history)
│   ├── basics/
│   ├── dictionaries/
│   ├── conditionals/
│   └── snake_game/
├── tests/                 # pytest suite
├── scripts/               # dev helpers (lint + test)
├── .github/workflows/     # CI
├── pyproject.toml
├── requirements-dev.txt
└── README.md
```

## Quickstart

Requires Python 3.10+.

```bash
git clone https://github.com/arunb-lab/pyforge.git
cd pyforge

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\\Scripts\\Activate.ps1

python -m pip install -U pip
python -m pip install -r requirements-dev.txt
```

## Running the projects

### FastAPI service

```bash
python -m pip install fastapi uvicorn httpx
uvicorn src.fastapi_service.app:create_app --factory --reload
```

Then open `http://127.0.0.1:8000/healthz` and `http://127.0.0.1:8000/docs`.

### DateRange CLI

```bash
python -m src.daterange.cli 2026-01-01..2026-01-31
python -m src.daterange.cli 2026-01-01..2026-01-31 --business-days
python -m src.daterange.cli 2026-01-01..2026-01-31 --split 7
```

### Heatmap (SVG)

```bash
python -m src.heatmap.cli --counts counts.json --last-days 365 --out heatmap.svg
```

## Development

```bash
pytest          # run the test suite
ruff check .    # lint
```

## License

Released under the [MIT License](LICENSE).
