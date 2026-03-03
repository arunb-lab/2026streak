import pytest

from project.dsa.tree_euler_tour import euler_tour, is_ancestor


def test_euler_tour_properties() -> None:
    edges = [(0, 1), (0, 2), (1, 3), (1, 4)]
    parent, depth, tin, tout, order = euler_tour(5, edges, root=0)

    assert parent[0] == -1
    assert depth[0] == 0
    assert len(order) == 5
    assert sorted(order) == [0, 1, 2, 3, 4]

    # Ancestor checks.
    assert is_ancestor(0, 4, tin, tout)
    assert is_ancestor(1, 4, tin, tout)
    assert not is_ancestor(2, 4, tin, tout)


def test_disconnected_raises() -> None:
    with pytest.raises(ValueError):
        euler_tour(3, [(0, 1)], root=0)
