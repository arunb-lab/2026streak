"""DSA - Arrays: Rotate Array

Problem:
Rotate the array to the right by k steps, in-place.

In-place via reversals:
1) Reverse whole array
2) Reverse first k
3) Reverse the rest

Time: O(n)
Space: O(1)
"""

from __future__ import annotations


def rotate(nums: list[int], k: int) -> None:
    n = len(nums)
    if n == 0:
        return
    k %= n

    def rev(l: int, r: int) -> None:
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    rev(0, n - 1)
    rev(0, k - 1)
    rev(k, n - 1)


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7]
    rotate(a, 3)
    assert a == [5, 6, 7, 1, 2, 3, 4]

    b = [-1, -100, 3, 99]
    rotate(b, 2)
    assert b == [3, 99, -1, -100]
    print("ok")
