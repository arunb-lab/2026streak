"""Quick sort reference implementations.

Includes:
- In-place Lomuto partition quicksort
- A safer randomized pivot variant

Complexity:
- Average: O(n log n)
- Worst: O(n^2)

Note: Python's built-in `sorted()` uses Timsort and is usually better.
"""

from __future__ import annotations

import random
from typing import List, MutableSequence, TypeVar

T = TypeVar("T")


def quick_sort_in_place(a: MutableSequence[T]) -> None:
    """Sort `a` in-place using quicksort (Lomuto partition)."""
    if len(a) <= 1:
        return
    _qs(a, 0, len(a) - 1)


def quick_sort_randomized_in_place(a: MutableSequence[T], *, seed: int | None = None) -> None:
    """Quicksort with randomized pivot to reduce chance of worst-case inputs."""
    if seed is not None:
        random.seed(seed)
    if len(a) <= 1:
        return
    _qs_random(a, 0, len(a) - 1)


def _qs(a: MutableSequence[T], lo: int, hi: int) -> None:
    if lo >= hi:
        return
    p = _partition_lomuto(a, lo, hi)
    _qs(a, lo, p - 1)
    _qs(a, p + 1, hi)


def _qs_random(a: MutableSequence[T], lo: int, hi: int) -> None:
    if lo >= hi:
        return
    pivot_index = random.randint(lo, hi)
    a[pivot_index], a[hi] = a[hi], a[pivot_index]
    p = _partition_lomuto(a, lo, hi)
    _qs_random(a, lo, p - 1)
    _qs_random(a, p + 1, hi)


def _partition_lomuto(a: MutableSequence[T], lo: int, hi: int) -> int:
    pivot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi] = a[hi], a[i]
    return i


def _demo() -> None:
    nums: List[int] = [3, 6, 8, 10, 1, 2, 1]
    quick_sort_in_place(nums)
    print(nums)

    nums2: List[int] = [5, 4, 3, 2, 1]
    quick_sort_randomized_in_place(nums2, seed=1)
    print(nums2)


if __name__ == "__main__":
    _demo()
