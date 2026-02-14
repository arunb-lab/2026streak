"""DSA - Arrays: Product of Array Except Self

Problem:
Return an array answer such that answer[i] is the product of all elements of nums
except nums[i], without using division.

Approach:
- Prefix products in output
- Multiply by suffix product in reverse pass

Time: O(n)
Space: O(1) extra (output excluded)
"""

from __future__ import annotations


def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    out = [1] * n

    prefix = 1
    for i in range(n):
        out[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        out[i] *= suffix
        suffix *= nums[i]

    return out


if __name__ == "__main__":
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    print("ok")
