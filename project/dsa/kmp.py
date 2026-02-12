"""Knuth–Morris–Pratt (KMP) string search.

KMP finds occurrences of a pattern in a text in linear time.

Key idea:
- precompute an LPS/"pi" array for the pattern (longest proper prefix
  that is also a suffix)
- avoid re-checking characters by reusing previous matches

Complexities:
- build prefix table: O(m)
- search: O(n)
"""

from __future__ import annotations


def prefix_function(p: str) -> list[int]:
    """Compute the prefix-function (pi / LPS) for pattern p."""

    pi = [0] * len(p)
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = pi[j - 1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j
    return pi


def kmp_find_all(text: str, pattern: str) -> list[int]:
    """Return all start indices where pattern occurs in text."""

    if pattern == "":
        # Common convention: empty pattern matches at every position.
        return list(range(len(text) + 1))

    pi = prefix_function(pattern)
    res: list[int] = []

    j = 0
    for i, ch in enumerate(text):
        while j > 0 and ch != pattern[j]:
            j = pi[j - 1]
        if ch == pattern[j]:
            j += 1
            if j == len(pattern):
                res.append(i - len(pattern) + 1)
                j = pi[j - 1]

    return res
