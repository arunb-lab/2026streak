"""DSA - Hashing: Two Sum (Hash Map)

Problem:
Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target.

Note:
This repo already has an Arrays/Two Sum version. This file exists to emphasize
hashing as a technique and provide a clean reference implementation.

Approach:
- Store value -> index for values already seen.
- For each x, check if target-x exists.

Time: O(n)
Space: O(n)
"""

from __future__ import annotations


def two_sum_hash(nums: list[int], target: int) -> tuple[int, int]:
    seen: dict[int, int] = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return seen[need], i
        seen[x] = i
    raise ValueError("No two sum solution")


if __name__ == "__main__":
    assert two_sum_hash([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum_hash([3, 2, 4], 6) == (1, 2)
    print("ok")
