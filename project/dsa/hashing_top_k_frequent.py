from __future__ import annotations

from collections import Counter


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Return the k most frequent elements.

    Uses a frequency map (hash table) and Counter.most_common.

    Time:  O(n log k) typical (implementation-dependent)
    Space: O(n)
    """

    if k < 0:
        raise ValueError("k must be non-negative")
    if k == 0:
        return []
    if not nums:
        return []

    counts = Counter(nums)
    return [x for x, _ in counts.most_common(k)]
