"""Single Number (LeetCode 136).

Problem:
Given a non-empty array of integers where every element appears twice except for
one, find that single one.

Approach (XOR):
XOR has the properties:
- a ^ a = 0
- a ^ 0 = a
- XOR is associative and commutative
So XOR-ing all values cancels out the pairs and leaves the unique number.

Time:  O(n)
Space: O(1)
"""

from __future__ import annotations


def single_number(nums: list[int]) -> int:
    if not nums:
        raise ValueError("nums must be non-empty")

    x = 0
    for v in nums:
        x ^= v
    return x
