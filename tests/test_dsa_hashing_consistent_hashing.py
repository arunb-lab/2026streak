from project.dsa.hashing_consistent_hashing import ConsistentHashRing


def test_consistent_hash_ring_empty() -> None:
    r = ConsistentHashRing()
    assert r.get_node("k") is None


def test_consistent_hash_ring_add_get_remove() -> None:
    r = ConsistentHashRing(replicas=8)
    r.add_node("A")
    r.add_node("B")
    r.add_node("C")

    n = r.get_node("user:123")
    assert n in {"A", "B", "C"}

    r.remove_node("B")
    n2 = r.get_node("user:123")
    assert n2 in {"A", "C"}


def test_consistent_hash_ring_low_churn_on_add() -> None:
    # Adding one node should not move *most* keys.
    keys = [f"k{i}" for i in range(2000)]

    r = ConsistentHashRing(replicas=64)
    r.add_node("A")
    r.add_node("B")
    r.add_node("C")

    before = {k: r.get_node(k) for k in keys}

    r.add_node("D")
    after = {k: r.get_node(k) for k in keys}

    moved = sum(1 for k in keys if before[k] != after[k])
    # Rough expectation: ~1/(N+1) move => ~25% for N=3. Allow slack.
    assert moved / len(keys) < 0.40
