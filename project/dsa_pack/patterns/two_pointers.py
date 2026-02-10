from __future__ import annotations

from typing import List, Optional, Tuple


def pair_sum_sorted(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    """Return indices (i, j) such that nums[i] + nums[j] == target.

    Assumes nums is sorted (non-decreasing). Returns None if no pair exists.

    Time: O(n)
    Space: O(1)
    """

    i, j = 0, len(nums) - 1
    while i < j:
        s = nums[i] + nums[j]
        if s == target:
            return i, j
        if s < target:
            i += 1
        else:
            j -= 1
    return None


def remove_duplicates_sorted(nums: List[int]) -> int:
    """In-place remove duplicates from a sorted list.

    Returns k such that nums[:k] contains the unique values.

    Time: O(n)
    Space: O(1)
    """

    if not nums:
        return 0

    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1

    return write
