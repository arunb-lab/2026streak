import pytest

from project.dsa.sliding_window_maximum import max_sliding_window


def test_max_sliding_window_example() -> None:
    assert max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]


def test_max_sliding_window_edge_cases() -> None:
    assert max_sliding_window([4], 1) == [4]
    assert max_sliding_window([2, 2, 2], 2) == [2, 2]


def test_max_sliding_window_validation() -> None:
    with pytest.raises(ValueError):
        max_sliding_window([], 1)
    with pytest.raises(ValueError):
        max_sliding_window([1, 2, 3], 0)
    with pytest.raises(ValueError):
        max_sliding_window([1, 2, 3], 4)
