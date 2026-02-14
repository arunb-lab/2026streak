"""DSA - Arrays: Maximum Subarray (Kadane)

Problem:
Find the contiguous subarray with the largest sum.

Kadane's algorithm:
- Maintain best sum ending at i (curr)
- Either extend previous subarray or start new at i
- Track global best

Time: O(n)
Space: O(1)
"""

from __future__ import annotations


def max_subarray(nums: list[int]) -> int:
    if not nums:
        raise ValueError("nums must be non-empty")

    best = curr = nums[0]
    for x in nums[1:]:
        curr = max(x, curr + x)
        best = max(best, curr)
    return best


if __name__ == "__main__":
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6  # [4,-1,2,1]
    assert max_subarray([1]) == 1
    assert max_subarray([5, 4, -1, 7, 8]) == 23
    print("ok")
