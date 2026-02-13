"""Longest Common Subsequence (LCS).

Compute length of the LCS between two strings.

Time:  O(n*m)
Space: O(min(n, m)) with rolling DP.
"""

from __future__ import annotations


def lcs_length(a: str, b: str) -> int:
    if a == b:
        return len(a)

    # Keep b as the shorter one for memory.
    if len(b) > len(a):
        a, b = b, a

    prev = [0] * (len(b) + 1)

    for ca in a:
        cur = [0] * (len(b) + 1)
        for j, cb in enumerate(b, start=1):
            if ca == cb:
                cur[j] = prev[j - 1] + 1
            else:
                cur[j] = max(prev[j], cur[j - 1])
        prev = cur

    return prev[-1]
