import pytest

from project.dsa.unique_paths import unique_paths


def test_unique_paths_basic() -> None:
    assert unique_paths(3, 7) == 28
    assert unique_paths(3, 2) == 3
    assert unique_paths(1, 10) == 1
    assert unique_paths(10, 1) == 1


def test_unique_paths_invalid() -> None:
    with pytest.raises(ValueError):
        unique_paths(0, 5)
    with pytest.raises(ValueError):
        unique_paths(5, 0)
