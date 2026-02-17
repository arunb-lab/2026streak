# Merge Sort

**Idea:** divide the array into halves, sort each half, then merge two sorted halves.

- Time: `O(n log n)` (best/avg/worst)
- Space: `O(n)` extra (classic merge)
- Stable: yes

## Why `O(n log n)`?

- `log n` levels of recursion (halving each time)
- each level merges all items once (`O(n)` work)
- total: `O(n log n)`

## Python implementation

See: `DSA/notes/code/merge_sort.py`

