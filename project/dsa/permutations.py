"""Permutations (LeetCode 46).

Problem:
Given a list of distinct integers `nums`, return all possible permutations.

Approach (backtracking):
Build a permutation incrementally, tracking which indices are already used.

Time:  O(n · n!)  (n! permutations, O(n) to build/copy each)
Space: O(n) recursion + output
"""

from __future__ import annotations


def permutations(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    used = [False] * n
    cur: list[int] = []
    out: list[list[int]] = []

    def backtrack() -> None:
        if len(cur) == n:
            out.append(cur.copy())
            return
        for i in range(n):
            if used[i]:
                continue
            used[i] = True
            cur.append(nums[i])
            backtrack()
            cur.pop()
            used[i] = False

    backtrack()
    return out
