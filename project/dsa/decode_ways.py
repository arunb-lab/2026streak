"""Decode Ways (LeetCode 91).

Problem:
A message containing letters from A-Z can be encoded into numbers using:
A->1, B->2, ..., Z->26.
Given a digit string `s`, return the number of ways to decode it.

Approach (DP, O(1) memory):
Let dp[i] be the number of ways to decode s[:i].
Transitions depend on:
- single digit s[i-1] in 1..9
- two digits s[i-2:i] in 10..26

Time:  O(n)
Space: O(1)
"""

from __future__ import annotations


def decode_ways(s: str) -> int:
    if not s:
        return 0

    # dp0 = dp[i-2], dp1 = dp[i-1]
    dp0 = 1
    dp1 = 0 if s[0] == "0" else 1

    for i in range(2, len(s) + 1):
        ways = 0

        one = s[i - 1]
        if one != "0":
            ways += dp1

        two = s[i - 2 : i]
        if "10" <= two <= "26":
            ways += dp0

        dp0, dp1 = dp1, ways

    return dp1
