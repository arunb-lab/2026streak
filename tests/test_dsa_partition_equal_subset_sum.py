import pytest

from project.dsa.partition_equal_subset_sum import can_partition


def test_can_partition_examples() -> None:
    assert can_partition([1, 5, 11, 5]) is True
    assert can_partition([1, 2, 3, 5]) is False


def test_can_partition_small() -> None:
    assert can_partition([2, 2, 3, 5]) is False


def test_can_partition_requires_positive() -> None:
    with pytest.raises(ValueError):
        can_partition([1, 0, 1])
