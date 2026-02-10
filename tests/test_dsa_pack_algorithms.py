import unittest

from project.dsa_pack.algorithms.binary_search import binary_search, lower_bound
from project.dsa_pack.algorithms.dijkstra import build_directed_weighted, shortest_path_to
from project.dsa_pack.algorithms.graph_traversal import bfs_order, build_undirected_graph, dfs_order
from project.dsa_pack.algorithms.sorting import bubble_sort, merge_sort


class TestAlgorithms(unittest.TestCase):
    def test_sorting(self):
        nums = [3, 1, 2, 5, 4]
        self.assertEqual(bubble_sort(nums), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort(nums), [1, 2, 3, 4, 5])

    def test_binary_search(self):
        nums = [1, 3, 3, 5, 8]
        self.assertEqual(binary_search(nums, 5), 3)
        self.assertIsNone(binary_search(nums, 7))
        self.assertEqual(lower_bound(nums, 3), 1)
        self.assertEqual(lower_bound(nums, 4), 3)

    def test_bfs_dfs(self):
        g = build_undirected_graph([("A", "B"), ("A", "C"), ("B", "D")])
        self.assertEqual(bfs_order(g, "A"), ["A", "B", "C", "D"])
        self.assertEqual(dfs_order(g, "A"), ["A", "B", "D", "C"])

    def test_dijkstra(self):
        wg = build_directed_weighted([
            ("A", "B", 4),
            ("A", "C", 2),
            ("C", "B", 1),
            ("B", "D", 5),
            ("C", "D", 8),
        ])
        self.assertEqual(shortest_path_to(wg, "A", "B"), 3)
        self.assertEqual(shortest_path_to(wg, "A", "D"), 8)
        self.assertIsNone(shortest_path_to(wg, "D", "A"))


if __name__ == "__main__":
    unittest.main()
