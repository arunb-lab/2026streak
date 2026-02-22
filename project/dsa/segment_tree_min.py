"""Segment tree for Range Minimum Query (RMQ).

Supports:
- build from list
- point update
- range_min query on [l, r) half-open interval

Time:
- Build: O(n)
- Update: O(log n)
- Query: O(log n)
"""

from __future__ import annotations

from math import inf


class SegmentTreeMin:
    def __init__(self, arr: list[float]) -> None:
        self.n = len(arr)
        size = 1
        while size < self.n:
            size <<= 1
        self.size = size
        self.t = [inf] * (2 * size)

        # build
        for i, x in enumerate(arr):
            self.t[size + i] = float(x)
        for i in range(size - 1, 0, -1):
            self.t[i] = min(self.t[2 * i], self.t[2 * i + 1])

    def range_min(self, l: int, r: int) -> float:
        if l < 0 or r < 0 or l > r or r > self.n:
            raise ValueError("invalid range")
        if l == r:
            return inf

        l += self.size
        r += self.size
        res = inf
        while l < r:
            if l & 1:
                res = min(res, self.t[l])
                l += 1
            if r & 1:
                r -= 1
                res = min(res, self.t[r])
            l >>= 1
            r >>= 1
        return res

    def update(self, idx: int, value: float) -> None:
        if not (0 <= idx < self.n):
            raise IndexError("index out of range")
        i = self.size + idx
        self.t[i] = float(value)
        i //= 2
        while i >= 1:
            self.t[i] = min(self.t[2 * i], self.t[2 * i + 1])
            i //= 2
