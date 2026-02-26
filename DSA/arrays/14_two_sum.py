"""DSA - Arrays: Two Sum

Problem:
Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target.

Assumptions (common LeetCode variant):
- Exactly one solution exists
- Cannot use the same element twice

Approach:
Use a hash map from number -> index seen so far.

Time: O(n)
Space: O(n)
"""

from __future__ import annotations


def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    seen: dict[int, int] = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return (seen[need], i)
        seen[x] = i

    raise ValueError("no two sum solution")


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum([3, 2, 4], 6) == (1, 2)
    assert two_sum([3, 3], 6) == (0, 1)
    print("ok")
