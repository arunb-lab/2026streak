"""Binary search patterns.

Binary search isn't only for "find an element".
It's also for "find the boundary" where a predicate flips from False -> True.
"""

from __future__ import annotations


def lower_bound(nums: list[int], x: int) -> int:
    """First index i where nums[i] >= x (like C++ lower_bound).

    If all elements are < x, returns len(nums).

    Time: O(log n)
    """

    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def search_rotated_sorted(nums: list[int], target: int) -> int:
    """Search target in a rotated sorted array (no duplicates).

    Returns index if found, else -1.

    Time: O(log n)
    """

    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid

        if nums[lo] <= nums[mid]:
            # Left half is sorted.
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            # Right half is sorted.
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1

    return -1
