"""DSA - Strings: Longest Palindromic Substring

Problem:
Given a string s, return the longest palindromic substring.

Approach (expand around center):
- A palindrome is defined by its center.
- For each index, expand for odd-length (i,i) and even-length (i,i+1).
- Track best window.

Time: O(n^2)
Space: O(1)
"""

from __future__ import annotations


def _expand(s: str, l: int, r: int) -> tuple[int, int]:
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return l + 1, r  # half-open [l, r)


def longest_palindrome(s: str) -> str:
    if not s:
        return ""

    best_l, best_r = 0, 1

    for i in range(len(s)):
        l1, r1 = _expand(s, i, i)
        if r1 - l1 > best_r - best_l:
            best_l, best_r = l1, r1

        l2, r2 = _expand(s, i, i + 1)
        if r2 - l2 > best_r - best_l:
            best_l, best_r = l2, r2

    return s[best_l:best_r]


if __name__ == "__main__":
    assert longest_palindrome("babad") in {"bab", "aba"}
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") in {"a", "c"}
    print("ok")
