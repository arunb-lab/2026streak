from __future__ import annotations

from collections.abc import Iterable
from typing import TypeVar

T = TypeVar("T")


def contains_duplicate(items: Iterable[T]) -> bool:
    """Return True if any value appears at least twice.

    This is the canonical "hash set" use-case.

    Time:  O(n)
    Space: O(n) in the worst case (all unique)
    """

    seen: set[T] = set()
    for x in items:
        if x in seen:
            return True
        seen.add(x)
    return False
