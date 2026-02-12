import unittest

from project.dsa_pack.patterns.prefix_sum import (
    build_prefix,
    count_subarrays_sum_k,
    range_sum,
)
from project.dsa_pack.patterns.sliding_window import (
    longest_substring_without_repeats,
    max_sum_subarray_k,
)
from project.dsa_pack.patterns.two_pointers import (
    pair_sum_sorted,
    remove_duplicates_sorted,
)


class TestPatterns(unittest.TestCase):
    def test_pair_sum_sorted(self):
        self.assertEqual(pair_sum_sorted([1, 2, 3, 4, 6], 6), (1, 3))
        self.assertIsNone(pair_sum_sorted([1, 2, 3], 100))

    def test_remove_duplicates_sorted(self):
        nums = [1, 1, 2, 2, 3]
        k = remove_duplicates_sorted(nums)
        self.assertEqual(k, 3)
        self.assertEqual(nums[:k], [1, 2, 3])

    def test_max_sum_subarray_k(self):
        self.assertEqual(max_sum_subarray_k([1, 2, 3, 4, 5], 2), 9)
        self.assertIsNone(max_sum_subarray_k([1, 2], 3))

    def test_longest_substring_without_repeats(self):
        self.assertEqual(longest_substring_without_repeats("abcabcbb"), 3)
        self.assertEqual(longest_substring_without_repeats("bbbbb"), 1)
        self.assertEqual(longest_substring_without_repeats(""), 0)

    def test_prefix_sum(self):
        nums = [2, -1, 3, 1]
        prefix = build_prefix(nums)
        self.assertEqual(range_sum(prefix, 0, 2), 4)
        self.assertEqual(count_subarrays_sum_k([1, 1, 1], 2), 2)


if __name__ == "__main__":
    unittest.main()
