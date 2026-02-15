import pytest

from project.dsa.hashing_top_k_frequent import top_k_frequent


def test_top_k_frequent_basic() -> None:
    out = top_k_frequent([1, 1, 1, 2, 2, 3], 2)
    assert set(out) == {1, 2}


def test_top_k_frequent_k_zero() -> None:
    assert top_k_frequent([1, 2, 3], 0) == []


def test_top_k_frequent_empty() -> None:
    assert top_k_frequent([], 3) == []


def test_top_k_frequent_invalid_k() -> None:
    with pytest.raises(ValueError):
        top_k_frequent([1], -1)
