"""Merge sort (stable) implementation.

This is written for clarity.

Complexity:
- Time: O(n log n)
- Space: O(n)

Notes:
- Python's built-in `sorted()` is usually preferable in real code.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Sequence, TypeVar

T = TypeVar("T")


def merge_sort(arr: Sequence[T]) -> List[T]:
    """Return a new list containing the elements of `arr` in sorted order."""
    n = len(arr)
    if n <= 1:
        return list(arr)

    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: Sequence[T], right: Sequence[T]) -> List[T]:
    i = j = 0
    out: List[T] = []

    # Stable merge: if equal, prefer left.
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1

    if i < len(left):
        out.extend(left[i:])
    if j < len(right):
        out.extend(right[j:])

    return out


@dataclass(frozen=True, order=True)
class Person:
    age: int
    name: str


def _demo() -> None:
    nums = [5, 2, 4, 7, 1, 3, 2, 6]
    print("nums:", nums)
    print("sorted:", merge_sort(nums))

    # Stability demo: same age keeps input order of names.
    people = [Person(20, "A"), Person(20, "B"), Person(19, "C"), Person(20, "D")]
    print("people:", people)
    print("sorted:", merge_sort(people))


if __name__ == "__main__":
    _demo()
