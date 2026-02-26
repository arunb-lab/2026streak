"""DSA - Sorting: Merge Sort

Problem:
Sort an array of integers.

Merge sort:
- Divide the array into halves
- Recursively sort each half
- Merge two sorted halves

This implementation returns a NEW sorted list (does not mutate input).

Time: O(n log n)
Space: O(n)
"""

from __future__ import annotations


def merge_sort(nums: list[int]) -> list[int]:
    n = len(nums)
    if n <= 1:
        return nums[:]

    mid = n // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return _merge(left, right)


def _merge(a: list[int], b: list[int]) -> list[int]:
    out: list[int] = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1

    if i < len(a):
        out.extend(a[i:])
    if j < len(b):
        out.extend(b[j:])

    return out


if __name__ == "__main__":
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    assert merge_sort([3, 1, 2]) == [1, 2, 3]
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert merge_sort([2, 2, 1]) == [1, 2, 2]
    print("ok")
