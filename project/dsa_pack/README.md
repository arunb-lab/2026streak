# project/dsa_pack

A beginner-friendly DSA pack implemented in **pure Python** (stdlib-only code).

This is a mono-package containing five mini-project areas:

- `patterns/` — common problem-solving patterns
- `data_structures/` — classic data structures from scratch
- `algorithms/` — sorting, searching, graph traversal
- `cli_visualizer/` — tiny CLI that prints step-by-step traces
- `benchmarks/` — simple `timeit` benchmarks (learning-focused)

## Run tests

From repo root:

```bash
pytest -q
# or
python -m unittest -v
```

## Run the CLI visualizer

```bash
python -m project.dsa_pack.cli_visualizer.cli bfs --start A --edges A:B A:C B:D
python -m project.dsa_pack.cli_visualizer.cli dijkstra --start A --edges A:B:4 A:C:2 C:B:1 B:D:5 C:D:8
```
