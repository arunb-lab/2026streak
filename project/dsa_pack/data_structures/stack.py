from __future__ import annotations

from dataclasses import dataclass, field
from typing import Generic, Iterable, Iterator, List, Optional, TypeVar

T = TypeVar("T")


@dataclass
class Stack(Generic[T]):
    """A simple LIFO stack.

    Backed by a Python list.
    - push/pop are amortized O(1)
    """

    _data: List[T] = field(default_factory=list)

    @classmethod
    def from_iterable(cls, items: Iterable[T]) -> "Stack[T]":
        s: Stack[T] = cls()
        for x in items:
            s.push(x)
        return s

    def push(self, item: T) -> None:
        self._data.append(item)

    def pop(self) -> T:
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> Optional[T]:
        return self._data[-1] if self._data else None

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self) -> Iterator[T]:
        # Iterate from bottom to top (insertion order)
        return iter(self._data)
