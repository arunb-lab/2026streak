"""Two pointers patterns.

Two pointers is most useful when:
- the input is sorted (or can be sorted)
- you're scanning from both ends
- you're maintaining two indices that only move forward

The implementations below are small reference solutions with tests.
"""

from __future__ import annotations

from dataclasses import dataclass


def is_subsequence(s: str, t: str) -> bool:
    """Return True if `s` is a subsequence of `t`.

    Example:
        s="ace", t="abcde" -> True
        s="aec", t="abcde" -> False

    Time:  O(len(t))
    Space: O(1)
    """

    i = 0
    for ch in t:
        if i < len(s) and s[i] == ch:
            i += 1
            if i == len(s):
                return True
    return i == len(s)


@dataclass(frozen=True)
class PairResult:
    left: int
    right: int


def pair_with_sum_sorted(nums: list[int], target: int) -> PairResult | None:
    """Find indices (i, j) in a sorted list such that nums[i] + nums[j] == target.

    Returns the first found pair (by pointer movement), or None.

    Time:  O(n)
    Space: O(1)
    """

    i, j = 0, len(nums) - 1
    while i < j:
        s = nums[i] + nums[j]
        if s == target:
            return PairResult(i, j)
        if s < target:
            i += 1
        else:
            j -= 1
    return None
