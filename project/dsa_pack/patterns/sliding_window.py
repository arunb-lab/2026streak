from __future__ import annotations

from typing import Dict, List, Optional


def max_sum_subarray_k(nums: List[int], k: int) -> Optional[int]:
    """Return the maximum sum of any contiguous subarray of size k.

    Returns None if k is invalid.

    Time: O(n)
    Space: O(1)
    """

    if k <= 0 or k > len(nums):
        return None

    window_sum = sum(nums[:k])
    best = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        if window_sum > best:
            best = window_sum

    return best


def longest_substring_without_repeats(s: str) -> int:
    """Length of the longest substring with all unique characters.

    Sliding window with last-seen indices.

    Time: O(n)
    Space: O(min(n, alphabet))
    """

    last_seen: Dict[str, int] = {}
    left = 0
    best = 0

    for right, ch in enumerate(s):
        prev = last_seen.get(ch)
        if prev is not None and prev >= left:
            left = prev + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)

    return best
