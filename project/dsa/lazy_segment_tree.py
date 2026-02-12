"""Lazy Segment Tree (range add, range sum).

When you need to apply updates over *ranges* and still answer queries over ranges,
"lazy propagation" avoids pushing updates to every leaf.

Operations:
- range_add(l, r_exclusive, delta)
- range_sum(l, r_exclusive)

Complexities:
- update/query: O(log n)
- memory: O(n)

Notes:
- indices are 0-based and ranges are half-open [l, r)
"""

from __future__ import annotations


class LazySegTreeRangeAddSum:
    def __init__(self, nums: list[int]):
        self._n = len(nums)
        size = 1
        while size < self._n:
            size <<= 1
        self._size = size
        self._tree = [0] * (2 * size)
        self._lazy = [0] * (2 * size)

        for i, x in enumerate(nums):
            self._tree[size + i] = x
        for i in range(size - 1, 0, -1):
            self._tree[i] = self._tree[2 * i] + self._tree[2 * i + 1]

    @property
    def n(self) -> int:
        return self._n

    def _apply(self, idx: int, seg_len: int, delta: int) -> None:
        self._tree[idx] += delta * seg_len
        self._lazy[idx] += delta

    def _push(self, idx: int, seg_len: int) -> None:
        if self._lazy[idx] == 0 or idx >= self._size:
            return
        half = seg_len // 2
        delta = self._lazy[idx]
        self._apply(2 * idx, half, delta)
        self._apply(2 * idx + 1, half, delta)
        self._lazy[idx] = 0

    def range_add(self, left: int, right_exclusive: int, delta: int) -> None:
        if left < 0 or right_exclusive < left or right_exclusive > self._n:
            raise ValueError("invalid range")
        if left == right_exclusive or delta == 0:
            return
        self._range_add(1, 0, self._size, left, right_exclusive, delta)

    def _range_add(
        self,
        idx: int,
        seg_left: int,
        seg_right: int,
        ql: int,
        qr: int,
        delta: int,
    ) -> None:
        if ql <= seg_left and seg_right <= qr:
            self._apply(idx, seg_right - seg_left, delta)
            return
        self._push(idx, seg_right - seg_left)
        mid = (seg_left + seg_right) // 2
        if ql < mid:
            self._range_add(2 * idx, seg_left, mid, ql, min(qr, mid), delta)
        if qr > mid:
            self._range_add(2 * idx + 1, mid, seg_right, max(ql, mid), qr, delta)
        self._tree[idx] = self._tree[2 * idx] + self._tree[2 * idx + 1]

    def range_sum(self, left: int, right_exclusive: int) -> int:
        if left < 0 or right_exclusive < left or right_exclusive > self._n:
            raise ValueError("invalid range")
        if left == right_exclusive:
            return 0
        return self._range_sum(1, 0, self._size, left, right_exclusive)

    def _range_sum(
        self, idx: int, seg_left: int, seg_right: int, ql: int, qr: int
    ) -> int:
        if ql <= seg_left and seg_right <= qr:
            return self._tree[idx]
        self._push(idx, seg_right - seg_left)
        mid = (seg_left + seg_right) // 2
        res = 0
        if ql < mid:
            res += self._range_sum(2 * idx, seg_left, mid, ql, min(qr, mid))
        if qr > mid:
            res += self._range_sum(2 * idx + 1, mid, seg_right, max(ql, mid), qr)
        return res
