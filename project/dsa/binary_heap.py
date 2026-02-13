"""Binary min-heap (from scratch).

Python has `heapq`, but implementing a heap is a great DSA exercise.

This module provides a small MinHeap class supporting:
- push
- pop
- peek

Time:
- push/pop: O(log n)
- peek: O(1)
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class MinHeap:
    _a: list[int] = field(default_factory=list)

    def __len__(self) -> int:  # pragma: no cover
        return len(self._a)

    def peek(self) -> int:
        if not self._a:
            raise IndexError("peek from empty heap")
        return self._a[0]

    def push(self, x: int) -> None:
        a = self._a
        a.append(x)
        i = len(a) - 1
        while i > 0:
            p = (i - 1) // 2
            if a[p] <= a[i]:
                break
            a[p], a[i] = a[i], a[p]
            i = p

    def pop(self) -> int:
        a = self._a
        if not a:
            raise IndexError("pop from empty heap")
        if len(a) == 1:
            return a.pop()

        root = a[0]
        a[0] = a.pop()

        i = 0
        n = len(a)
        while True:
            l = 2 * i + 1
            r = 2 * i + 2
            smallest = i

            if l < n and a[l] < a[smallest]:
                smallest = l
            if r < n and a[r] < a[smallest]:
                smallest = r

            if smallest == i:
                break

            a[i], a[smallest] = a[smallest], a[i]
            i = smallest

        return root
