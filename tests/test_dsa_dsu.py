import pytest

from project.dsa.dsu import DSU, count_components


def test_dsu_union_find() -> None:
    d = DSU(5)
    assert d.components == 5

    assert d.union(0, 1) is True
    assert d.union(1, 2) is True
    assert d.union(0, 2) is False

    assert d.find(0) == d.find(2)
    assert d.components == 3

    with pytest.raises(IndexError):
        d.find(10)


def test_count_components() -> None:
    assert count_components(5, [(0, 1), (1, 2), (3, 4)]) == 2
    assert count_components(3, []) == 3
