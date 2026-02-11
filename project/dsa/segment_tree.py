"""Segment Tree (range sum query + point update).

This is a classic data structure when you need:
- many range queries
- with updates in between

Operations here:
- build from list
- update(i, value)
- query(l, r_exclusive)

Time:
- build: O(n)
- update: O(log n)
- query: O(log n)
"""

from __future__ import annotations


class SegmentTreeSum:
    def __init__(self, nums: list[int]):
        self.n = len(nums)
        # Next power of two size.
        size = 1
        while size < self.n:
            size <<= 1
        self.size = size
        self.tree = [0] * (2 * size)

        # Build leaves.
        for i, x in enumerate(nums):
            self.tree[self.size + i] = x
        # Build internal nodes.
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index: int, value: int) -> None:
        if index < 0 or index >= self.n:
            raise IndexError("index out of range")
        i = self.size + index
        self.tree[i] = value
        i //= 2
        while i >= 1:
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
            i //= 2

    def query(self, left: int, right_exclusive: int) -> int:
        if left < 0 or right_exclusive < left or right_exclusive > self.n:
            raise ValueError("invalid range")

        l = self.size + left
        r = self.size + right_exclusive
        res = 0

        while l < r:
            if l & 1:
                res += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                res += self.tree[r]
            l //= 2
            r //= 2

        return res
