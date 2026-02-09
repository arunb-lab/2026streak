"""API error helpers.

Not strictly required for a demo service, but shows how to centralize
consistent error responses.
"""

from __future__ import annotations

from pydantic import BaseModel


class ErrorResponse(BaseModel):
    error: str
    detail: str
