from __future__ import annotations

import httpx
import pytest

from flagship_fastapi_service.flagship_api.app import create_app
from flagship_fastapi_service.flagship_api.version import SERVICE_NAME, SERVICE_VERSION


def _async_client() -> httpx.AsyncClient:
    app = create_app()
    transport = httpx.ASGITransport(app=app)
    return httpx.AsyncClient(transport=transport, base_url="http://test")


@pytest.mark.anyio
async def test_healthz_ok() -> None:
    async with _async_client() as client:
        res = await client.get("/healthz")

    assert res.status_code == 200
    assert res.json() == {"status": "ok"}


@pytest.mark.anyio
async def test_version() -> None:
    async with _async_client() as client:
        res = await client.get("/version")

    assert res.status_code == 200
    assert res.json() == {"name": SERVICE_NAME, "version": SERVICE_VERSION}
