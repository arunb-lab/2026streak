"""Z-algorithm for pattern matching.

The Z-array for a string s is defined as:
- z[0] = 0
- z[i] = length of the longest substring starting at i which is also a prefix of s

Applications:
- Find all occurrences of pattern in text in O(n+m) time by computing Z on:
  pattern + '$' + text.

Ref: https://cp-algorithms.com/string/z-function.html
"""

from __future__ import annotations


def z_function(s: str) -> list[int]:
    """Compute Z-array for s."""
    n = len(s)
    z = [0] * n
    left = 0
    right = 0

    for i in range(1, n):
        if i <= right:
            z[i] = min(right - i + 1, z[i - left])

        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        if i + z[i] - 1 > right:
            left = i
            right = i + z[i] - 1

    return z


def z_find_all(text: str, pattern: str) -> list[int]:
    """Return starting indices where ``pattern`` occurs in ``text``.

    Empty pattern matches at every position including the end.
    """
    if pattern == "":
        return list(range(len(text) + 1))

    combined = pattern + "$" + text
    z = z_function(combined)

    out: list[int] = []
    m = len(pattern)
    for i in range(m + 1, len(combined)):
        if z[i] >= m:
            out.append(i - (m + 1))

    return out
