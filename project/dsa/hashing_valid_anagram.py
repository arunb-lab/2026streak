from __future__ import annotations

from collections import Counter


def is_anagram(a: str, b: str) -> bool:
    """Return True if a and b are anagrams (same multiset of characters).

    Uses a frequency map (hash table).

    Time:  O(n)
    Space: O(1) for fixed alphabet, otherwise O(k) unique chars
    """

    # Fast-path for obvious mismatch.
    if len(a) != len(b):
        return False

    return Counter(a) == Counter(b)
