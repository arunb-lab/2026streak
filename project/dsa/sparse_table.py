"""Sparse Table (static range query).

A sparse table preprocesses an array for fast *static* range queries.
It works best for idempotent operations (min/max/gcd) where:
    op(x, x) == x

This module provides a Range Minimum Query (RMQ) implementation.

Complexities:
- build:  O(n log n)
- query:  O(1)
- memory: O(n log n)

If you need updates, prefer a Segment Tree or Fenwick Tree.
"""

from __future__ import annotations



class SparseTableMin:
    def __init__(self, nums: list[int]):
        self._n = len(nums)
        if self._n == 0:
            self._k = 0
            self._st: list[list[int]] = []
            self._log: list[int] = [0]
            return

        self._k = (self._n).bit_length()
        self._st = [nums[:] ]

        j = 1
        while (1 << j) <= self._n:
            prev = self._st[j - 1]
            span = 1 << (j - 1)
            cur = [min(prev[i], prev[i + span]) for i in range(self._n - (1 << j) + 1)]
            self._st.append(cur)
            j += 1

        # Precompute logs for query.
        self._log = [0] * (self._n + 1)
        for i in range(2, self._n + 1):
            self._log[i] = self._log[i // 2] + 1

    @property
    def n(self) -> int:
        return self._n

    def query(self, left: int, right_exclusive: int) -> int:
        """Return min(nums[left:right_exclusive])."""

        if left < 0 or right_exclusive < left or right_exclusive > self._n:
            raise ValueError("invalid range")
        if left == right_exclusive:
            raise ValueError("empty range")

        length = right_exclusive - left
        j = self._log[length]
        span = 1 << j
        a = self._st[j][left]
        b = self._st[j][right_exclusive - span]
        return a if a < b else b
