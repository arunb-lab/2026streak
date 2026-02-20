from project.dsa.binary_tree import build_tree_level_order
from project.dsa.binary_tree_max_depth import max_depth_bfs, max_depth_dfs


def test_max_depth_examples() -> None:
    assert max_depth_dfs(build_tree_level_order([3, 9, 20, None, None, 15, 7])) == 3
    assert max_depth_bfs(build_tree_level_order([3, 9, 20, None, None, 15, 7])) == 3


def test_max_depth_empty() -> None:
    assert max_depth_dfs(None) == 0
    assert max_depth_bfs(None) == 0
