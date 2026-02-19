"""Sliding Window Maximum (Monotonic Deque).

Given an array ``nums`` and a window size ``k``, compute the maximum value in every
contiguous window of size ``k``.

This is a classic monotonic-queue application:
- Maintain a deque of indices with values in *decreasing* order.
- The front of the deque is always the index of the current window maximum.

Time complexity: O(n)
Space complexity: O(k)

Ref: https://leetcode.com/problems/sliding-window-maximum/
"""

from __future__ import annotations

from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    """Return the maximum for each sliding window of size ``k``.

    Args:
        nums: Input list.
        k: Window size (must satisfy 1 <= k <= len(nums)).

    Raises:
        ValueError: If ``k`` is not within [1, len(nums)].

    Examples:
        >>> max_sliding_window([1,3,-1,-3,5,3,6,7], 3)
        [3, 3, 5, 5, 6, 7]
    """

    n = len(nums)
    if k <= 0 or k > n:
        raise ValueError("k must satisfy 1 <= k <= len(nums)")

    dq: deque[int] = deque()  # indices, nums[dq] decreasing
    out: list[int] = []

    for i, x in enumerate(nums):
        # Remove indices outside the window [i-k+1, i]
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Maintain decreasing order (drop smaller/equal values from the back)
        while dq and nums[dq[-1]] <= x:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            out.append(nums[dq[0]])

    return out
