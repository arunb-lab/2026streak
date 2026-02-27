"""Product of array except self.

Problem:
Given an integer array nums, return an array answer such that answer[i] is the
product of all the elements of nums except nums[i].

Constraints typically disallow division and require O(n).

Approach:
- Prefix products (product of elements left of i)
- Suffix products (product of elements right of i)
Combine in one pass each.

Time: O(n)
Space: O(1) extra (excluding output)
"""

from __future__ import annotations


def product_except_self(nums: list[int]) -> list[int]:
    if not nums:
        return []

    out = [1] * len(nums)

    prefix = 1
    for i, x in enumerate(nums):
        out[i] = prefix
        prefix *= x

    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        out[i] *= suffix
        suffix *= nums[i]

    return out
