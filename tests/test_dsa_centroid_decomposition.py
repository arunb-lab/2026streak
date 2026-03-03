from project.dsa.centroid_decomposition import CentroidDecomposition


def test_centroid_decomposition_line_tree() -> None:
    # Line: 0-1-2-3-4-5-6
    n = 7
    edges = [(i, i + 1) for i in range(n - 1)]
    cd = CentroidDecomposition(n, edges)

    # Exactly one root centroid with parent -1.
    roots = [i for i, p in enumerate(cd.centroid_parent) if p == -1]
    assert len(roots) == 1

    # Levels are non-negative and root has level 0.
    r = roots[0]
    assert cd.level[r] == 0
    assert all(lvl >= 0 for lvl in cd.level)

    # Parent pointers form a tree (no self-parent).
    for i in range(n):
        assert cd.centroid_parent[i] != i
