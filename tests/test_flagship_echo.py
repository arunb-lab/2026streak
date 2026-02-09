from __future__ import annotations

import httpx
import pytest

from flagship_fastapi_service.flagship_api.app import create_app


def _async_client() -> httpx.AsyncClient:
    transport = httpx.ASGITransport(app=create_app())
    return httpx.AsyncClient(transport=transport, base_url="http://test")


@pytest.mark.anyio
async def test_echo_roundtrip() -> None:
    async with _async_client() as client:
        res = await client.post("/echo", json={"message": "hello"})

    assert res.status_code == 200
    assert res.json() == {"message": "hello"}


@pytest.mark.anyio
async def test_echo_rejects_empty_message() -> None:
    async with _async_client() as client:
        res = await client.post("/echo", json={"message": ""})

    assert res.status_code == 422
