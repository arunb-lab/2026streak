"""Runtime configuration.

This is intentionally simple and environment-variable driven.
"""

from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(frozen=True, slots=True)
class Settings:
    environment: str = os.getenv("ENVIRONMENT", "dev")
    log_level: str = os.getenv("LOG_LEVEL", "info")


def get_settings() -> Settings:
    return Settings()
