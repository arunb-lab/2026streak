import unittest

from project.dsa_pack.cli_visualizer.traces import bfs_trace, dijkstra_trace


class TestCliVisualizerTraces(unittest.TestCase):
    def test_bfs_trace(self):
        steps = bfs_trace(edges=[("A", "B"), ("A", "C"), ("B", "D")], start="A")
        self.assertTrue(steps)
        self.assertEqual(steps[0].current, "A")
        self.assertIn("B", steps[-1].seen)
        self.assertIn("D", steps[-1].seen)

    def test_dijkstra_trace(self):
        steps = dijkstra_trace(
            edges=[
                ("A", "B", 4),
                ("A", "C", 2),
                ("C", "B", 1),
                ("B", "D", 5),
                ("C", "D", 8),
            ],
            start="A",
        )
        self.assertTrue(steps)
        # after completion, best known dist to B is 3
        final_dist = steps[-1].dist_snapshot
        self.assertEqual(final_dist["B"], 3)


if __name__ == "__main__":
    unittest.main()
