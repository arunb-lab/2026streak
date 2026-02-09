from __future__ import annotations

import httpx
import pytest

from flagship_fastapi_service.flagship_api.app import create_app


def _async_client() -> httpx.AsyncClient:
    transport = httpx.ASGITransport(app=create_app())
    return httpx.AsyncClient(transport=transport, base_url="http://test")


@pytest.mark.anyio
async def test_todo_crud_happy_path() -> None:
    async with _async_client() as client:
        # empty list
        res = await client.get("/todos")
        assert res.status_code == 200
        assert res.json() == []

        # create
        res = await client.post("/todos", json={"title": "ship it"})
        assert res.status_code == 201
        todo = res.json()
        assert todo["title"] == "ship it"
        assert todo["done"] is False
        assert "id" in todo
        assert "created_at" in todo
        todo_id = todo["id"]

        # get
        res = await client.get(f"/todos/{todo_id}")
        assert res.status_code == 200
        assert res.json()["id"] == todo_id

        # update
        res = await client.patch(f"/todos/{todo_id}", json={"done": True})
        assert res.status_code == 200
        assert res.json()["done"] is True

        # list now has one
        res = await client.get("/todos")
        assert res.status_code == 200
        assert len(res.json()) == 1

        # delete
        res = await client.delete(f"/todos/{todo_id}")
        assert res.status_code == 204

        # gone
        res = await client.get("/todos")
        assert res.status_code == 200
        assert res.json() == []


@pytest.mark.anyio
async def test_todo_not_found_is_400_value_error() -> None:
    async with _async_client() as client:
        res = await client.get("/todos/does-not-exist")

    assert res.status_code == 400
    body = res.json()
    assert body["error"] == "value_error"
