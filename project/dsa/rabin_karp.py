"""Rabin–Karp string search (rolling hash).

Find all occurrences of a pattern in a text.

Notes:
- Rolling hash can have collisions. We *verify* matches by comparing slices.
- Uses a single modulus/base suitable for typical ASCII/UTF-8 Python strings.

Time complexity:
- Expected: O(n + m)
- Worst-case (many collisions): O(n*m) due to verification.
"""

from __future__ import annotations


def rabin_karp_find_all(text: str, pattern: str) -> list[int]:
    """Return starting indices where ``pattern`` occurs in ``text``.

    By convention, an empty pattern matches at every position including the end.
    """
    n, m = len(text), len(pattern)
    if m == 0:
        return list(range(n + 1))
    if m > n:
        return []

    base = 911382323
    mod = 1_000_000_007

    # Precompute base^(m-1)
    high_pow = 1
    for _ in range(m - 1):
        high_pow = (high_pow * base) % mod

    def _hash(s: str) -> int:
        h = 0
        for ch in s:
            h = (h * base + ord(ch)) % mod
        return h

    ph = _hash(pattern)
    wh = _hash(text[:m])

    out: list[int] = []

    def _maybe_add(i: int) -> None:
        if wh == ph and text[i : i + m] == pattern:
            out.append(i)

    _maybe_add(0)

    for i in range(1, n - m + 1):
        left = ord(text[i - 1])
        right = ord(text[i + m - 1])

        # Remove left char: wh - left * base^(m-1)
        wh = (wh - left * high_pow) % mod
        # Shift and add right char
        wh = (wh * base + right) % mod

        _maybe_add(i)

    return out
