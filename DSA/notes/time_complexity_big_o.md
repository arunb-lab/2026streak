# Time Complexity (Big-O)

Big-O is a **growth-rate upper bound**: how fast runtime increases as input size `n` increases.
It ignores constant factors and lower-order terms.

> Big-O answers: “For sufficiently large `n`, runtime is **at most proportional** to …”.

## Common growth rates (from fast to slow)

- `O(1)` — constant (hash lookup *expected*, array index access)
- `O(log n)` — logarithmic (binary search, balanced BST ops)
- `O(n)` — linear (single pass)
- `O(n log n)` — linearithmic (comparison sorting lower bound)
- `O(n^2)` — quadratic (nested loops over pairs)
- `O(2^n)` — exponential (subset enumeration)
- `O(n!)` — factorial (permutations)

### Quick intuition
- `log n` means you “halve the problem” each step.
- `n log n` often means: “do `log n` levels of work, each level touches `n` items” (merge sort).

## Best / Average / Worst case

Some algorithms vary with input distribution:

- Quick sort: average `O(n log n)`, worst `O(n^2)` (bad pivots)
- Hash table lookup: expected `O(1)`, worst `O(n)` (pathological collisions)

When writing complexity, prefer:

- **Worst-case** when you need hard guarantees.
- **Expected / average** when randomness or typical inputs make it realistic.

## Tight bounds vs upper bounds

- `O(f(n))` — upper bound
- `Ω(f(n))` — lower bound
- `Θ(f(n))` — tight (both upper and lower)

Example:

- For comparison sorting, worst-case time is `Θ(n log n)`.

## Space complexity

Space usually counts **extra memory beyond the input**.

- Merge sort: `O(n)` extra space (classic version)
- Quick sort: `O(log n)` extra space (recursion stack average)

## Quick practice table

| Task | Typical approach | Time | Space |
|---|---|---:|---:|
| Find max in array | single pass | `O(n)` | `O(1)` |
| Check membership | hash set | expected `O(1)` | `O(n)` |
| Sort numbers | `sorted()` (Timsort) | `O(n log n)` worst | `O(n)` |

## Rule of thumb

- If `n` can be ~10^5, you generally want `O(n log n)` or better.
- If `n` can be ~10^6, `O(n)` or `O(n log n)` with small constants.
- Exponential (`2^n`) usually caps at `n ≈ 25..30`.

