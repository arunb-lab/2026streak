# `project.dsa` — Advanced Python DSA references

Small, readable implementations (with tests) for common data structures & algorithms.

## Data structures

- `dsu.py` — Disjoint Set Union (Union-Find)
- `fenwick_tree.py` — Fenwick Tree / BIT (prefix sums + order-statistics helper)
- `segment_tree.py` — Segment Tree (range sum + point update)
- `lazy_segment_tree.py` — Lazy Segment Tree (range add + range sum)
- `sparse_table.py` — Sparse Table (static range minimum query)
- `trie.py` — Trie / prefix tree
- `lru_cache.py` — LRU cache (OrderedDict-based)

## Graph algorithms

- `graph_traversal.py` — BFS shortest path, topo sort (DFS)
- `topological_sort.py` — topo sort (Kahn / in-degree)
- `dijkstra.py` — Dijkstra shortest paths (non-negative weights)
- `bellman_ford.py` — shortest paths with negative-weight support (+ cycle detection)
- `lca_binary_lifting.py` — LCA on trees via binary lifting

## Patterns

- `two_pointers.py`
- `sliding_window.py`
- `prefix_sums.py`
- `binary_search.py`
- `monotonic_stack.py`

## Strings

- `kmp.py` — KMP substring search

---

Run tests:

```bash
pytest
```

Lint:

```bash
ruff check .
```
