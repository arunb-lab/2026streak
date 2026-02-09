"""FastAPI application entrypoint.

Use the app factory so the service is easy to test and deploy.
"""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request

from .errors import ErrorResponse
from .models import EchoRequest, EchoResponse, HealthResponse, VersionResponse
from .settings import get_settings
from .version import SERVICE_NAME, SERVICE_VERSION


def create_app() -> FastAPI:
    settings = get_settings()

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

    return app
