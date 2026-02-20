from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass(slots=True)
class MinStack(Generic[T]):
    """Stack that supports retrieving current minimum in O(1) time.

    Implementation stores pairs: (value, min_so_far).

    Raises:
        IndexError on pop/top/get_min when empty.
    """

    _st: list[tuple[T, T]]

    def __init__(self) -> None:
        self._st = []

    def __len__(self) -> int:
        return len(self._st)

    def push(self, x: T) -> None:
        if not self._st:
            self._st.append((x, x))
            return
        cur_min = self._st[-1][1]
        self._st.append((x, x if x < cur_min else cur_min))

    def pop(self) -> T:
        if not self._st:
            raise IndexError("pop from empty MinStack")
        return self._st.pop()[0]

    def top(self) -> T:
        if not self._st:
            raise IndexError("top from empty MinStack")
        return self._st[-1][0]

    def get_min(self) -> T:
        if not self._st:
            raise IndexError("get_min from empty MinStack")
        return self._st[-1][1]

    def try_get_min(self) -> Optional[T]:
        return self._st[-1][1] if self._st else None
