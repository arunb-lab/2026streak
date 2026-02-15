import pytest

from project.dsa.hashing_design_hashmap import HashMap


def test_hashmap_put_get_update_remove() -> None:
    m: HashMap[str, int] = HashMap(initial_capacity=2)

    assert len(m) == 0
    assert m.get("missing") is None

    m.put("a", 1)
    m.put("b", 2)
    assert len(m) == 2
    assert m.get("a") == 1
    assert m.get("b") == 2

    # update
    m.put("a", 10)
    assert len(m) == 2
    assert m.get("a") == 10

    # remove
    assert m.remove("a") is True
    assert m.get("a") is None
    assert len(m) == 1
    assert m.remove("a") is False


def test_hashmap_resizes_and_keeps_entries() -> None:
    m: HashMap[int, int] = HashMap(initial_capacity=2, load_factor=0.6)
    for i in range(100):
        m.put(i, i * i)

    assert len(m) == 100
    for i in range(100):
        assert m.get(i) == i * i


def test_hashmap_validation() -> None:
    with pytest.raises(ValueError):
        HashMap(initial_capacity=0)
    with pytest.raises(ValueError):
        HashMap(load_factor=0.01)
