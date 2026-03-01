"""Partition Equal Subset Sum (LeetCode 416).

Problem:
Given a non-empty array `nums` of positive integers, determine if it can be
partitioned into two subsets such that the sums are equal.

Approach:
This is a subset-sum to `total//2`.
Use a bitset DP where bit i indicates whether sum i is achievable.

Time:  O(n * target/word_bits) effectively, but implemented with Python int shifts.
Space: O(1) extra (bitset integer)
"""

from __future__ import annotations


def can_partition(nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2 == 1:
        return False

    target = total // 2
    bits = 1  # sum 0 achievable
    for x in nums:
        if x <= 0:
            raise ValueError("nums must contain positive integers")
        bits |= bits << x
        # Optional mask to keep integer small.
        if bits.bit_length() > target + 1:
            bits &= (1 << (target + 1)) - 1

    return ((bits >> target) & 1) == 1
