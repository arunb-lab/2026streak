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
- `min_stack.py` — MinStack (O(1) min retrieval)

## Graph algorithms

- `graph_traversal.py` — BFS shortest path, topo sort (DFS)
- `topological_sort.py` — topo sort (Kahn / in-degree)
- `dijkstra.py` — Dijkstra shortest paths (non-negative weights)
- `bellman_ford.py` — shortest paths with negative-weight support (+ cycle detection)
- `lca_binary_lifting.py` — LCA on trees via binary lifting

## Trees & linked lists

- `binary_tree.py` — `TreeNode` + level-order build/serialize helpers
- `binary_tree_traversals.py` — preorder/inorder/postorder (recursive + iterative)
- `binary_tree_level_order.py` — level-order traversal
- `binary_tree_max_depth.py` — tree maximum depth (DFS/BFS)
- `validate_bst.py` — BST validation (bounds recursion)
- `bst_kth_smallest.py` — kth-smallest in BST (iterative inorder)
- `bst_lca.py` — LCA in BST (iterative)
- `merge_k_sorted_lists.py` — merge k sorted linked lists (heap)

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
python -m pytest
```

Lint:

```bash
ruff check .
```
