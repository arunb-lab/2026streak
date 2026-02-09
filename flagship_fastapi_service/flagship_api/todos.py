"""A tiny in-memory Todo store.

This is intentionally simple (no DB) but structured in a way that could be
swapped for a real persistence layer.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Dict, List
from uuid import uuid4


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


@dataclass(slots=True)
class Todo:
    id: str
    title: str
    done: bool
    created_at: datetime


class TodoStore:
    def __init__(self) -> None:
        self._items: Dict[str, Todo] = {}

    def list(self) -> List[Todo]:
        # stable order for tests / predictable UX
        return sorted(self._items.values(), key=lambda t: t.created_at)

    def create(self, title: str) -> Todo:
        todo = Todo(id=str(uuid4()), title=title, done=False, created_at=utc_now())
        self._items[todo.id] = todo
        return todo

    def get(self, todo_id: str) -> Todo:
        try:
            return self._items[todo_id]
        except KeyError as e:
            raise ValueError(f"todo not found: {todo_id}") from e

    def set_done(self, todo_id: str, done: bool) -> Todo:
        todo = self.get(todo_id)
        todo.done = done
        return todo

    def delete(self, todo_id: str) -> None:
        if todo_id not in self._items:
            raise ValueError(f"todo not found: {todo_id}")
        del self._items[todo_id]
