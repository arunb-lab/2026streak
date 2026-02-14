"""DSA - Arrays: Merge Sorted Array

Problem:
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n. Merge nums2 into nums1 as one sorted array.

Classic in-place from the back:
- i = m-1, j = n-1, k = m+n-1
- place the larger of nums1[i] / nums2[j] at nums1[k]

Time: O(m+n)
Space: O(1)
"""

from __future__ import annotations


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1


if __name__ == "__main__":
    a = [1, 2, 3, 0, 0, 0]
    merge(a, 3, [2, 5, 6], 3)
    assert a == [1, 2, 2, 3, 5, 6]

    b = [0]
    merge(b, 0, [1], 1)
    assert b == [1]
    print("ok")
