import pytest

from project.dsa.min_path_sum_grid import min_path_sum


def test_min_path_sum_example() -> None:
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1],
    ]
    assert min_path_sum(grid) == 7


def test_min_path_sum_single_cell() -> None:
    assert min_path_sum([[5]]) == 5


def test_min_path_sum_empty_raises() -> None:
    with pytest.raises(ValueError):
        min_path_sum([])
