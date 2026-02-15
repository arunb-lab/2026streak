from __future__ import annotations

from collections import defaultdict


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group words that are anagrams.

    Key idea: anagrams share the same character-count signature.
    We use a tuple of 26 counts for lowercase a-z.

    Time:  O(n * m)
      n = number of words, m = average word length
    Space: O(n)
    """

    groups: dict[tuple[int, ...], list[str]] = defaultdict(list)

    for w in words:
        counts = [0] * 26
        for ch in w:
            idx = ord(ch) - ord("a")
            if idx < 0 or idx >= 26:
                raise ValueError("group_anagrams expects lowercase a-z words")
            counts[idx] += 1
        groups[tuple(counts)].append(w)

    return list(groups.values())
