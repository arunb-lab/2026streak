"""Sliding window patterns.

A sliding window maintains a contiguous region [l..r] while updating an invariant.
Common uses:
- fixed-size windows (e.g., max sum of size k)
- variable windows with constraints (e.g., at most K distinct chars)
"""

from __future__ import annotations

from collections import Counter


def max_sum_subarray_k(nums: list[int], k: int) -> int:
    """Return the maximum sum of any contiguous subarray of length k.

    Raises:
        ValueError: if k <= 0 or k > len(nums)

    Time:  O(n)
    Space: O(1)
    """

    if k <= 0 or k > len(nums):
        raise ValueError("k must be in [1, len(nums)]")

    window_sum = sum(nums[:k])
    best = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        if window_sum > best:
            best = window_sum

    return best


def longest_substring_k_distinct(s: str, k: int) -> int:
    """Length of the longest substring with at most k distinct characters.

    Time:  O(n)
    Space: O(k)
    """

    if k <= 0 or not s:
        return 0

    freq: Counter[str] = Counter()
    left = 0
    best = 0

    for r, ch in enumerate(s):
        freq[ch] += 1

        while len(freq) > k:
            left_ch = s[left]
            freq[left_ch] -= 1
            if freq[left_ch] == 0:
                del freq[left_ch]
            left += 1

        best = max(best, r - left + 1)

    return best
