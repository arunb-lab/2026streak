import pytest

from project.dsa.knapsack_01 import knapsack_01_max_value


def test_knapsack_01_basic() -> None:
    weights = [10, 20, 30]
    values = [60, 100, 120]
    assert knapsack_01_max_value(weights, values, 50) == 220


def test_knapsack_01_zero_capacity() -> None:
    assert knapsack_01_max_value([1, 2], [10, 20], 0) == 0


def test_knapsack_01_validation() -> None:
    with pytest.raises(ValueError):
        knapsack_01_max_value([1], [1, 2], 10)
    with pytest.raises(ValueError):
        knapsack_01_max_value([1], [1], -1)
