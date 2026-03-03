from project.dsa.virtual_tree import VirtualTreeBuilder


def test_virtual_tree_basic() -> None:
    # Tree:
    # 0-1, 0-2, 1-3, 1-4, 2-5
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5)]
    b = VirtualTreeBuilder(6, edges, root=0)

    vt = b.build([3, 4, 5])
    # Needed nodes: 3,4,5 plus lca(3,4)=1 and lca(1,5)=0.
    assert set(vt.nodes) == {0, 1, 3, 4, 5}
    assert vt.root == 0

    # Structure should be 0 -> {1,5} and 1 -> {3,4}
    assert set(vt.adj[0]) == {1, 5}
    assert set(vt.adj[1]) == {3, 4}
