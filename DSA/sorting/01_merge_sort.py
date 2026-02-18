"""DSA - Sorting: Merge Sort

Problem:
Sort a list of comparable items.

Approach (divide and conquer):
- Split the array into halves, sort each half, merge sorted halves.
- Stable sort.

Time: O(n log n)
Space: O(n)
"""

from __future__ import annotations


def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums[:]

    mid = len(nums) // 2
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
    assert merge_sort([5, -1, 5, 2, 0]) == [-1, 0, 2, 5, 5]
    print("ok")
