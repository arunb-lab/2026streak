"""Suffix Array + LCP (Kasai).

The suffix array SA of a string s is an array of starting indices of suffixes
in lexicographic order.

This implementation uses the classic O(n log n) doubling algorithm.
- Works for arbitrary Python strings.
- Returns SA as a list[int]

Also provides LCP array via Kasai in O(n):
- lcp[i] = LCP length of suffixes SA[i] and SA[i-1] (with lcp[0]=0)

Refs:
- Manber & Myers (1993)
- Kasai et al. (2001)
"""

from __future__ import annotations


def suffix_array(s: str) -> list[int]:
    n = len(s)
    if n == 0:
        return []

    # Initial ranking by character code.
    sa = list(range(n))
    rank = [ord(c) for c in s]
    tmp = [0] * n

    k = 1
    while True:
        sa.sort(key=lambda i: (rank[i], rank[i + k] if i + k < n else -1))

        tmp[sa[0]] = 0
        classes = 1
        for idx in range(1, n):
            i, j = sa[idx - 1], sa[idx]
            prev = (rank[i], rank[i + k] if i + k < n else -1)
            curr = (rank[j], rank[j + k] if j + k < n else -1)
            if curr != prev:
                classes += 1
            tmp[j] = classes - 1

        rank, tmp = tmp, rank
        if classes == n:
            break
        k <<= 1

    return sa


def lcp_array(s: str, sa: list[int]) -> list[int]:
    """Kasai algorithm: compute LCP array for s given its suffix array."""

    n = len(s)
    if n == 0:
        return []
    if len(sa) != n:
        raise ValueError("sa must have length len(s)")

    pos = [0] * n
    for i, p in enumerate(sa):
        pos[p] = i

    lcp = [0] * n
    k = 0
    for i in range(n):
        r = pos[i]
        if r == 0:
            k = 0
            continue
        j = sa[r - 1]
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1
        lcp[r] = k
        if k:
            k -= 1

    return lcp
