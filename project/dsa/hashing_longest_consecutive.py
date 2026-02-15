from __future__ import annotations


def longest_consecutive(nums: list[int]) -> int:
    """Return the length of the longest consecutive sequence.

    Classic hash-set trick:
    - Put all numbers into a set
    - Only start counting from numbers that are sequence starts (x-1 not present)

    Time:  O(n) expected
    Space: O(n)
    """

    s = set(nums)
    best = 0

    for x in s:
        if x - 1 in s:
            # not a sequence start
            continue

        y = x
        while y in s:
            y += 1
        best = max(best, y - x)

    return best
