from __future__ import annotations

from typing import List


def bubble_sort(nums: List[int]) -> List[int]:
    """Return a sorted copy using bubble sort (teaching algorithm).

    Time: O(n^2)
    Space: O(1) extra (ignoring output copy)
    """

    arr = nums[:]
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def merge_sort(nums: List[int]) -> List[int]:
    """Return a sorted copy using merge sort.

    Time: O(n log n)
    Space: O(n)
    """

    if len(nums) <= 1:
        return nums[:]

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return _merge(left, right)


def _merge(a: List[int], b: List[int]) -> List[int]:
    out: List[int] = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    out.extend(a[i:])
    out.extend(b[j:])
    return out
