"""Tiny task utilities.

This file is intentionally small, but kept clean:
- type hints
- explicit error handling
- no unused imports
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


DEFAULT_TASKS_PATH = Path("tasks.json")


def load_tasks(path: Path = DEFAULT_TASKS_PATH) -> list[dict[str, Any]]:
    """Load tasks from JSON.

    Returns an empty list if the file doesn't exist or contains invalid JSON.
    """

    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_tasks(tasks: list[dict[str, Any]], path: Path = DEFAULT_TASKS_PATH) -> None:
    payload = json.dumps(tasks, indent=2, ensure_ascii=False) + "\n"
    path.write_text(payload, encoding="utf-8")


def suggest_task(tasks: list[dict[str, Any]]) -> dict[str, Any] | None:
    """Return the easiest pending task (least time spent), or None."""

    pending = [t for t in tasks if not t.get("done", False)]
    if not pending:
        return None
    return min(pending, key=lambda t: int(t.get("time_spent", 0)))
