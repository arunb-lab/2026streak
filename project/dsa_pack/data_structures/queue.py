from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from typing import Deque, Generic, Iterable, Iterator, Optional, TypeVar

T = TypeVar("T")


@dataclass
class Queue(Generic[T]):
    """A simple FIFO queue.

    Backed by collections.deque.
    - enqueue/dequeue are O(1)
    """

    _data: Deque[T] = field(default_factory=deque)

    @classmethod
    def from_iterable(cls, items: Iterable[T]) -> "Queue[T]":
        q: Queue[T] = cls()
        for x in items:
            q.enqueue(x)
        return q

    def enqueue(self, item: T) -> None:
        self._data.append(item)

    def dequeue(self) -> T:
        if not self._data:
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def peek(self) -> Optional[T]:
        return self._data[0] if self._data else None

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self) -> Iterator[T]:
        return iter(self._data)
