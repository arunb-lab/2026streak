from project.dsa.meet_in_the_middle_subset_sum import subset_sum_exists


def test_subset_sum_exists_basic() -> None:
    assert subset_sum_exists([3, 34, 4, 12, 5, 2], 9) is True  # 4+5
    assert subset_sum_exists([3, 34, 4, 12, 5, 2], 30) is False


def test_subset_sum_exists_empty() -> None:
    assert subset_sum_exists([], 0) is True
    assert subset_sum_exists([], 1) is False


def test_subset_sum_exists_with_negatives() -> None:
    assert subset_sum_exists([1, -2, 4], 2) is True  # -2 + 4
