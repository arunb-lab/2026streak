"""Version info for the flagship service.

Kept in a dedicated module so it can be imported by both the app and tests
without creating circular imports.
"""

from __future__ import annotations

SERVICE_NAME: str = "flagship-fastapi-service"
SERVICE_VERSION: str = "0.1.0"
