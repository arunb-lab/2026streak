"""Pydantic models used by the API."""

from __future__ import annotations

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str = Field(examples=["ok"])


class VersionResponse(BaseModel):
    name: str
    version: str


class EchoRequest(BaseModel):
    message: str = Field(min_length=1, max_length=500)


class EchoResponse(BaseModel):
    message: str


class TodoCreateRequest(BaseModel):
    title: str = Field(min_length=1, max_length=140)


class TodoResponse(BaseModel):
    id: str
    title: str
    done: bool
    created_at: str


class TodoUpdateRequest(BaseModel):
    done: bool
