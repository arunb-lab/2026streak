from project.dsa.search_in_rotated_sorted_array import search_rotated


def test_search_rotated_examples() -> None:
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search_rotated([1], 0) == -1


def test_search_rotated_not_rotated() -> None:
    assert search_rotated([1, 2, 3, 4, 5], 4) == 3
