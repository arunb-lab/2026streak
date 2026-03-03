import pytest

from project.dsa.dsu_rollback import DSURollback


def test_dsu_rollback_basic() -> None:
    d = DSURollback(5)
    t0 = d.snapshot()
    assert d.components == 5

    assert d.union(0, 1)
    assert d.union(1, 2)
    assert d.components == 3

    t1 = d.snapshot()
    assert d.union(3, 4)
    assert d.components == 2

    d.rollback(t1)
    assert d.components == 3
    assert d.find(3) != d.find(4)

    d.rollback(t0)
    assert d.components == 5
    assert d.find(0) != d.find(1)


def test_invalid_token() -> None:
    d = DSURollback(1)
    with pytest.raises(ValueError):
        d.rollback(2)
