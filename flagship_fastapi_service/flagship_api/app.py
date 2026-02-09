"""FastAPI application entrypoint.

Use the app factory so the service is easy to test and deploy.
"""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request

from .errors import ErrorResponse
from .models import (
    EchoRequest,
    EchoResponse,
    HealthResponse,
    TodoCreateRequest,
    TodoResponse,
    TodoUpdateRequest,
    VersionResponse,
)
from .settings import get_settings
from .todos import TodoStore
from .version import SERVICE_NAME, SERVICE_VERSION


def create_app() -> FastAPI:
    settings = get_settings()
    store = TodoStore()

    app = FastAPI(
        title="Flagship FastAPI Service",
        version=SERVICE_VERSION,
        description="A small but production-leaning FastAPI example.",
    )

    @app.exception_handler(ValueError)
    async def value_error_handler(
        request: Request, exc: ValueError
    ) -> JSONResponse:  # pragma: no cover (FastAPI plumbing)
        _ = request
        payload = ErrorResponse(error="value_error", detail=str(exc))
        return JSONResponse(status_code=400, content=payload.model_dump())

    @app.get("/healthz", response_model=HealthResponse, tags=["meta"])
    def healthz() -> HealthResponse:
        # Keep it boring and reliable.
        _ = settings  # referenced to make it obvious settings are loaded
        return HealthResponse(status="ok")

    @app.get("/version", response_model=VersionResponse, tags=["meta"])
    def version() -> VersionResponse:
        return VersionResponse(name=SERVICE_NAME, version=SERVICE_VERSION)

    @app.post("/echo", response_model=EchoResponse, tags=["demo"])
    def echo(payload: EchoRequest) -> EchoResponse:
        return EchoResponse(message=payload.message)

    def _todo_to_response(todo) -> TodoResponse:
        return TodoResponse(
            id=todo.id,
            title=todo.title,
            done=todo.done,
            created_at=todo.created_at.isoformat(),
        )

    @app.get("/todos", response_model=list[TodoResponse], tags=["todos"])
    def list_todos() -> list[TodoResponse]:
        return [_todo_to_response(t) for t in store.list()]

    @app.post("/todos", response_model=TodoResponse, status_code=201, tags=["todos"])
    def create_todo(payload: TodoCreateRequest) -> TodoResponse:
        todo = store.create(title=payload.title)
        return _todo_to_response(todo)

    @app.get("/todos/{todo_id}", response_model=TodoResponse, tags=["todos"])
    def get_todo(todo_id: str) -> TodoResponse:
        todo = store.get(todo_id)
        return _todo_to_response(todo)

    @app.patch("/todos/{todo_id}", response_model=TodoResponse, tags=["todos"])
    def update_todo(todo_id: str, payload: TodoUpdateRequest) -> TodoResponse:
        todo = store.set_done(todo_id, done=payload.done)
        return _todo_to_response(todo)

    @app.delete("/todos/{todo_id}", status_code=204, tags=["todos"])
    def delete_todo(todo_id: str) -> None:
        store.delete(todo_id)
        return None

    return app
