"""Fenwick Tree (Binary Indexed Tree).

A Fenwick Tree supports prefix sums with point updates in O(log n).

Typical use-cases:
- dynamic prefix sums / range sums
- inversion counting
- order statistics (with find_by_prefix)

This implementation:
- uses 1-based indexing internally
- supports build from list in O(n log n)

Complexities:
- add/update: O(log n)
- prefix_sum / range_sum: O(log n)
- memory: O(n)
"""

from __future__ import annotations


class FenwickTree:
    def __init__(self, n: int):
        if n < 0:
            raise ValueError("n must be >= 0")
        self._n = n
        self._bit = [0] * (n + 1)  # index 0 unused

    @property
    def n(self) -> int:
        return self._n

    @classmethod
    def from_list(cls, nums: list[int]) -> "FenwickTree":
        ft = cls(len(nums))
        for i, x in enumerate(nums):
            ft.add(i, x)
        return ft

    def add(self, index: int, delta: int) -> None:
        """Add delta to nums[index]."""

        if index < 0 or index >= self._n:
            raise IndexError("index out of range")
        i = index + 1
        while i <= self._n:
            self._bit[i] += delta
            i += i & -i

    def prefix_sum(self, right_exclusive: int) -> int:
        """Sum of nums[0:right_exclusive]."""

        if right_exclusive < 0 or right_exclusive > self._n:
            raise ValueError("right_exclusive out of range")
        s = 0
        i = right_exclusive
        while i > 0:
            s += self._bit[i]
            i -= i & -i
        return s

    def range_sum(self, left: int, right_exclusive: int) -> int:
        """Sum of nums[left:right_exclusive]."""

        if left < 0 or right_exclusive < left or right_exclusive > self._n:
            raise ValueError("invalid range")
        return self.prefix_sum(right_exclusive) - self.prefix_sum(left)

    def find_by_prefix(self, target: int) -> int:
        """Smallest idx i such that prefix_sum(i+1) >= target.

        This is useful for order statistics when all values are non-negative.

        Args:
            target: 1-based prefix target. Must satisfy 1 <= target <= total_sum.

        Returns:
            index in [0, n-1]

        Raises:
            ValueError: if target is out of range.
        """

        total = self.prefix_sum(self._n)
        if target <= 0 or target > total:
            raise ValueError("target out of range")

        # Binary lifting over Fenwick tree.
        idx = 0
        bitmask = 1
        while bitmask <= self._n:
            bitmask <<= 1
        bitmask >>= 1

        cur = 0
        while bitmask:
            nxt = idx + bitmask
            if nxt <= self._n and cur + self._bit[nxt] < target:
                cur += self._bit[nxt]
                idx = nxt
            bitmask >>= 1

        # idx is the largest position where prefix sum < target.
        return idx  # 0-based because idx is count of elements strictly below target
