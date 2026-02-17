# Sorting Overview

Sorting algorithms are often compared along:

- **Time complexity** (best/avg/worst)
- **Space complexity** (extra memory)
- **Stability** (does it preserve the order of equal keys?)
- **In-place** (does it use only O(1) extra space, ignoring recursion stack?)

## Key properties

### Stable sort
A sort is **stable** if equal elements keep their original relative order.

Why it matters:

- Multi-key sorting: sort by secondary key, then stable-sort by primary key.

Examples:

- Merge sort: stable (classic implementation)
- Timsort (Python `sorted`): stable
- Quick sort: typically *not* stable (unless implemented with extra memory)

### In-place sort
“In-place” usually means `O(1)` extra storage (but recursion stack may be `O(log n)`).

Examples:

- Heap sort: in-place, not stable
- Quick sort: in-place partition, recursion stack `O(log n)` average

## Comparison model lower bound

If a sort only learns about order via comparisons (“is a < b?”), then in the worst case it needs:

- **Ω(n log n)** comparisons.

Reason (intuition):

- There are `n!` possible orderings.
- Each comparison provides at most 1 bit of information.
- Decision tree depth must be at least `log2(n!) = Θ(n log n)`.

So to do better than `O(n log n)`, you must use extra structure (e.g., integer ranges): counting/radix sorts.

## When to pick what

- **General-purpose**: Timsort (`sorted`) — great real-world performance, stable.
- **Need worst-case guarantees**: merge sort / heap sort.
- **Average-case speed, low memory**: quick sort (with good pivot strategy).
- **Integers in small range**: counting sort (`O(n + k)`).
- **Fixed-width integers/strings**: radix sort (often `O(d·(n + k))`).

