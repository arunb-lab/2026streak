import pytest

from project.dsa.lru_cache import LRUCache


def test_lru_cache_get_put_and_eviction() -> None:
    c: LRUCache[str, int] = LRUCache(2)

    assert c.get("a") is None

    c.put("a", 1)
    c.put("b", 2)
    assert len(c) == 2

    # Access a, making it MRU
    assert c.get("a") == 1
    assert c.keys_mru_to_lru() == ["a", "b"]

    # Insert c, should evict LRU (b)
    c.put("c", 3)
    assert c.get("b") is None
    assert c.get("c") == 3
    assert c.get("a") == 1

    st = c.stats()
    assert st.hits >= 1
    assert st.misses >= 1
    assert st.evictions == 1


def test_lru_cache_update_existing_key() -> None:
    c: LRUCache[int, str] = LRUCache(2)
    c.put(1, "x")
    c.put(2, "y")

    c.put(1, "xx")
    assert c.get(1) == "xx"
    assert c.keys_mru_to_lru()[0] == 1


def test_lru_cache_invalid_capacity() -> None:
    with pytest.raises(ValueError):
        LRUCache(0)
