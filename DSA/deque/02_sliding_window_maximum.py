"""DSA - Deque: Sliding Window Maximum

Problem:
Given an array nums and window size k, return the maximum for each sliding
window.

Approach (monotonic deque of indices):
Maintain indices in decreasing order of values.
- Remove indices that are out of the window from the left
- While the new value is >= values at the right, pop right (maintain decreasing)
- The leftmost index is the max for the current window

Time: O(n)
Space: O(k)
"""

from __future__ import annotations


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    if k <= 0:
        raise ValueError("k must be positive")
    if not nums:
        return []

    dq: list[int] = []  # indices, values decreasing
    out: list[int] = []

    for i, x in enumerate(nums):
        # drop out-of-window indices
        left_bound = i - k + 1
        if dq and dq[0] < left_bound:
            dq.pop(0)

        # maintain decreasing values
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)

        if i >= k - 1:
            out.append(nums[dq[0]])

    return out


if __name__ == "__main__":
    assert max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert max_sliding_window([1], 1) == [1]
    assert max_sliding_window([9, 11], 2) == [11]
    print("ok")
