"""DSA - Strings: Valid Anagram

Problem:
Given two strings s and t, return True if t is an anagram of s, and False otherwise.

Approach (frequency map):
- If lengths differ -> False
- Count characters in s
- Decrement counts while scanning t
- If any count drops below 0 -> False

Time: O(n)
Space: O(k) where k is the alphabet size (or unique chars)
"""

from __future__ import annotations

from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    counts = Counter(s)
    for ch in t:
        counts[ch] -= 1
        if counts[ch] < 0:
            return False
    return True


if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("aacc", "ccac") is False
    print("ok")
