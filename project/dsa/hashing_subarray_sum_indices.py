from __future__ import annotations


def first_subarray_sum_k(nums: list[int], k: int) -> tuple[int, int] | None:
    """Return (l, r) indices of the first subarray whose sum is k.

    The returned interval is half-open: nums[l:r].

    Uses prefix sums with a hash map from prefix_sum -> earliest index.

    Example:
        nums = [1, 2, 3], k = 3 => (0, 2) because [1, 2]

    Time:  O(n)
    Space: O(n)
    """

    prefix_to_idx: dict[int, int] = {0: 0}  # prefix sum 0 occurs before index 0
    prefix = 0

    for i, x in enumerate(nums, start=1):
        prefix += x
        need = prefix - k

        if need in prefix_to_idx:
            l = prefix_to_idx[need]
            r = i
            return (l, r)

        # keep earliest index to return the first occurrence
        if prefix not in prefix_to_idx:
            prefix_to_idx[prefix] = i

    return None
