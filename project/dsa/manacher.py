"""Manacher's algorithm for longest palindromic substring.

Computes the longest palindromic substring in linear time.

Technique:
Transform the string with separators to unify odd/even palindromes.
Example: "abba" -> "^#a#b#b#a#$".

Time complexity: O(n)
Space complexity: O(n)

Ref: https://cp-algorithms.com/string/manacher.html
"""

from __future__ import annotations


def longest_palindromic_substring(s: str) -> str:
    """Return one longest palindromic substring of ``s``."""
    if not s:
        return ""

    # Transform with sentinels to avoid bounds checks.
    t = "^#" + "#".join(s) + "#$"
    n = len(t)
    p = [0] * n

    center = 0
    right = 0

    for i in range(1, n - 1):
        mirror = 2 * center - i

        if i < right:
            p[i] = min(right - i, p[mirror])

        while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1

        if i + p[i] > right:
            center = i
            right = i + p[i]

    # Find max.
    max_len = 0
    max_center = 0
    for i, rad in enumerate(p):
        if rad > max_len:
            max_len = rad
            max_center = i

    start = (max_center - max_len) // 2
    return s[start : start + max_len]
