# Flagship FastAPI Service

A small, production-leaning FastAPI microservice intended as a “flagship-quality” example inside this repo.

## Features

- FastAPI app factory (`create_app()`)
- Health + version endpoints
- Typed request/response models
- In-memory Todo CRUD (demo)
- Tests using `pytest` + `httpx` (ASGI transport)

## Quickstart (local)

```bash
python -m venv .venv && source .venv/bin/activate
pip install -U pip
pip install fastapi uvicorn httpx pytest ruff

uvicorn flagship_fastapi_service.flagship_api.app:create_app --factory --reload
```

Open:
- http://127.0.0.1:8000/healthz
- http://127.0.0.1:8000/docs

## Project layout

```
flagship_fastapi_service/
  flagship_api/
  docs/
  scripts/
```
