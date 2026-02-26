"""DSA - Heap: Kth Largest Element in an Array

Problem:
Given an integer array nums and an integer k, return the k-th largest element.

Approach:
Maintain a min-heap of size k.
- Push each number
- If heap grows beyond k, pop smallest
- Heap root is k-th largest

Time: O(n log k)
Space: O(k)
"""

from __future__ import annotations

import heapq


def kth_largest(nums: list[int], k: int) -> int:
    if k <= 0:
        raise ValueError("k must be >= 1")
    if k > len(nums):
        raise ValueError("k cannot be larger than len(nums)")

    heap: list[int] = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


if __name__ == "__main__":
    assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    print("ok")
