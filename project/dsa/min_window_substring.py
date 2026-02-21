"""Minimum Window Substring (LeetCode 76).

Problem:
Given strings `s` and `t`, return the minimum window substring of `s` such that
every character in `t` (including multiplicity) is included in the window.
If there is no such substring, return the empty string.

Approach (sliding window with counts):
- Count required chars from `t`.
- Expand `right`, updating window counts and how many required chars are satisfied.
- When all are satisfied, shrink from the left to minimize.

Time:  O(|s| + |t|)
Space: O(|alphabet|)  (bounded by distinct chars in t)
"""

from __future__ import annotations

from collections import Counter, defaultdict


def min_window(s: str, t: str) -> str:
    if not t:
        return ""

    need = Counter(t)
    have: dict[str, int] = defaultdict(int)

    required = len(need)
    formed = 0

    best_len = float("inf")
    best_l = 0

    left = 0
    for right, ch in enumerate(s):
        have[ch] += 1
        if ch in need and have[ch] == need[ch]:
            formed += 1

        while formed == required and left <= right:
            window_len = right - left + 1
            if window_len < best_len:
                best_len = window_len
                best_l = left

            left_ch = s[left]
            have[left_ch] -= 1
            if left_ch in need and have[left_ch] < need[left_ch]:
                formed -= 1
            left += 1

    return "" if best_len == float("inf") else s[best_l : best_l + int(best_len)]
