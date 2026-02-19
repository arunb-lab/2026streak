"""Median of a Data Stream (Two Heaps).

Maintain the median of a stream of numbers as you insert elements.

Approach:
- A max-heap for the lower half (implemented by pushing negatives).
- A min-heap for the upper half.
- Rebalance so that either both halves have equal size or lower has one extra.

Time complexity:
- add(): O(log n)
- median(): O(1)

Ref: https://leetcode.com/problems/find-median-from-data-stream/
"""

from __future__ import annotations

import heapq


class MedianFinder:
    """Online median tracker."""

    def __init__(self) -> None:
        self._low: list[int] = []  # max-heap via negatives
        self._high: list[int] = []  # min-heap

    def __len__(self) -> int:
        return len(self._low) + len(self._high)

    def add(self, x: int) -> None:
        """Add a number to the stream."""
        if not self._low or x <= -self._low[0]:
            heapq.heappush(self._low, -x)
        else:
            heapq.heappush(self._high, x)

        # Rebalance sizes.
        if len(self._low) > len(self._high) + 1:
            heapq.heappush(self._high, -heapq.heappop(self._low))
        elif len(self._high) > len(self._low):
            heapq.heappush(self._low, -heapq.heappop(self._high))

    def median(self) -> float:
        """Return the current median.

        Raises:
            ValueError: If called on an empty stream.
        """
        if len(self) == 0:
            raise ValueError("median is undefined for an empty stream")

        if len(self._low) == len(self._high):
            return (-self._low[0] + self._high[0]) / 2.0
        return float(-self._low[0])
