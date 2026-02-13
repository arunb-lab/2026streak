"""Edit distance (Levenshtein distance).

Minimum number of single-character edits to turn s into t:
- insert
- delete
- substitute

Time:  O(n*m)
Space: O(min(n, m)) with rolling DP.
"""

from __future__ import annotations


def levenshtein_distance(s: str, t: str) -> int:
    if s == t:
        return 0

    # Make t the shorter string to minimize memory.
    if len(t) > len(s):
        s, t = t, s

    prev = list(range(len(t) + 1))

    for i, cs in enumerate(s, start=1):
        cur = [i] + [0] * len(t)
        for j, ct in enumerate(t, start=1):
            cost = 0 if cs == ct else 1
            cur[j] = min(
                prev[j] + 1,  # delete
                cur[j - 1] + 1,  # insert
                prev[j - 1] + cost,  # substitute
            )
        prev = cur

    return prev[-1]
