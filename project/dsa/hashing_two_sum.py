from __future__ import annotations


def two_sum_indices(nums: list[int], target: int) -> tuple[int, int] | None:
    """Return indices (i, j) such that nums[i] + nums[j] == target.

    Uses a hash map of value -> earliest index seen so far.

    Time:  O(n)
    Space: O(n)
    """

    seen: dict[int, int] = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return (seen[need], i)
        # keep the earliest index for stable output
        if x not in seen:
            seen[x] = i
    return None
