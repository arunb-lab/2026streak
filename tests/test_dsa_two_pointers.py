from project.dsa.two_pointers import is_subsequence, pair_with_sum_sorted


def test_is_subsequence_basic() -> None:
    assert is_subsequence("", "abc") is True
    assert is_subsequence("ace", "abcde") is True
    assert is_subsequence("aec", "abcde") is False
    assert is_subsequence("abc", "abc") is True
    assert is_subsequence("abcd", "abc") is False


def test_pair_with_sum_sorted() -> None:
    nums = [1, 2, 3, 4, 7, 11]
    r = pair_with_sum_sorted(nums, 9)
    assert r is not None
    assert nums[r.left] + nums[r.right] == 9

    assert pair_with_sum_sorted(nums, 100) is None
