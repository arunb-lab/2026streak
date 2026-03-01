"""Word Break (LeetCode 139).

Problem:
Given a string `s` and a list of words `word_dict`, return True if `s` can be
segmented into a space-separated sequence of one or more dictionary words.

Approach (DP):
Let dp[i] mean: s[:i] can be segmented.
- dp[0] = True
- dp[i] = any(dp[j] and s[j:i] in dict) for j < i

We optimize by only trying word lengths that exist in the dictionary.

Time:  O(n * k) where k is the number of distinct word lengths
Space: O(n)
"""

from __future__ import annotations


def word_break(s: str, word_dict: list[str]) -> bool:
    if s == "":
        return True
    if not word_dict:
        return False

    words = set(word_dict)
    lengths = sorted({len(w) for w in words})

    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for L in lengths:
            j = i - L
            if j < 0:
                break
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break

    return dp[n]
