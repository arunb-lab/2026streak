"""Combination Sum (LeetCode 39).

Problem:
Given an array of distinct integers `candidates` and an integer `target`, return
all unique combinations of candidates where the chosen numbers sum to target.
Each candidate may be chosen unlimited times.

Approach:
Backtracking with sorted candidates and non-decreasing index to avoid duplicates.

Time:  Exponential in general (output-sensitive)
Space: O(target/min(candidates)) recursion depth
"""

from __future__ import annotations


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    if target < 0:
        return []

    candidates = sorted(candidates)
    out: list[list[int]] = []

    def backtrack(start: int, remain: int, path: list[int]) -> None:
        if remain == 0:
            out.append(path.copy())
            return
        for i in range(start, len(candidates)):
            x = candidates[i]
            if x > remain:
                break
            path.append(x)
            backtrack(i, remain - x, path)
            path.pop()

    backtrack(0, target, [])
    return out
