from project.dsa.combination_sum import combination_sum


def test_combination_sum_examples() -> None:
    out = combination_sum([2, 3, 6, 7], 7)
    assert sorted(out) == sorted([[2, 2, 3], [7]])

    out2 = combination_sum([2, 3, 5], 8)
    assert sorted(out2) == sorted([[2, 2, 2, 2], [2, 3, 3], [3, 5]])


def test_combination_sum_zero_target() -> None:
    assert combination_sum([1, 2], 0) == [[]]
