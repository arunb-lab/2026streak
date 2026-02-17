# Quick Sort

**Idea:** pick a pivot, partition into elements `< pivot` and `>= pivot`, then recursively sort partitions.

- Average time: `O(n log n)`
- Worst time: `O(n^2)` (bad pivot choices)
- Space: `O(log n)` recursion stack average
- Stable: typically no (in-place partitioning scrambles equals)

## Why it is fast in practice

- In-place partitioning is cache-friendly.
- Constant factors are often smaller than merge sort.

## How to avoid worst-case

- Randomized pivot
- Median-of-three pivot
- Introsort (switch to heap sort if recursion depth is too high)

## Python implementation

See: `DSA/notes/code/quick_sort.py`

