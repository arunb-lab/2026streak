"""Quickselect (k-th smallest element).

Average-case O(n) selection using in-place partitioning (like quicksort).

- quickselect(nums, k): returns the k-th smallest element (0-indexed)

This mutates the input list.
"""

from __future__ import annotations

import random


def quickselect(nums: list[int], k: int) -> int:
    if not 0 <= k < len(nums):
        raise IndexError("k out of range")

    lo, hi = 0, len(nums) - 1

    while True:
        if lo == hi:
            return nums[lo]

        pivot_idx = random.randint(lo, hi)
        pivot = nums[pivot_idx]
        nums[pivot_idx], nums[hi] = nums[hi], nums[pivot_idx]

        # Lomuto partition
        store = lo
        for i in range(lo, hi):
            if nums[i] < pivot:
                nums[store], nums[i] = nums[i], nums[store]
                store += 1

        nums[store], nums[hi] = nums[hi], nums[store]

        if k == store:
            return nums[store]
        if k < store:
            hi = store - 1
        else:
            lo = store + 1
