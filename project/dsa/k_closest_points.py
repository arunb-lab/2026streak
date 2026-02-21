"""K Closest Points to Origin (LeetCode 973).

Problem:
Given an array of points on the X-Y plane, return the `k` points closest to the
origin (0, 0). Distance is Euclidean; we can compare squared distance.

Approach (size-k max-heap):
Keep a heap of at most k points with their *negative* squared distance.
- Push points while heap size < k
- Otherwise, if a point is closer than the farthest in heap, replace it

This is O(n log k) and works well when k << n.

Time:  O(n log k)
Space: O(k)
"""

from __future__ import annotations

import heapq


def k_closest(points: list[tuple[int, int]], k: int) -> list[tuple[int, int]]:
    if k < 0:
        raise ValueError("k must be non-negative")
    if k == 0 or not points:
        return []

    heap: list[tuple[int, tuple[int, int]]] = []  # (neg_dist2, point)

    for x, y in points:
        dist2 = x * x + y * y
        item = (-dist2, (x, y))
        if len(heap) < k:
            heapq.heappush(heap, item)
        else:
            # heap[0] is farthest (most negative distance -> largest dist2)
            if item > heap[0]:
                heapq.heapreplace(heap, item)

    return [p for _, p in heap]
