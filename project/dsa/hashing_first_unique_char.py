from __future__ import annotations

from collections import Counter


def first_unique_char_index(s: str) -> int:
    """Return the index of the first non-repeating character.

    Returns -1 if none exists.

    Time:  O(n)
    Space: O(k) distinct characters
    """

    counts = Counter(s)
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1
