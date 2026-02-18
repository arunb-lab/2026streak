"""DSA - Strings: Longest Substring Without Repeating Characters

Problem:
Given a string s, find the length of the longest substring without repeating
characters.

Approach (sliding window + last seen index):
- Maintain a window [left..right]
- Track last seen index for each character
- When we see a repeated char inside the window, move left to last_seen + 1

Time: O(n)
Space: O(k) where k is the number of distinct characters seen
"""

from __future__ import annotations


def length_of_longest_substring(s: str) -> int:
    last_seen: dict[str, int] = {}
    left = 0
    best = 0

    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)

    return best


if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    print("ok")
