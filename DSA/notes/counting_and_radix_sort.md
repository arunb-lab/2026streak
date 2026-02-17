# Counting Sort & Radix Sort

These algorithms can beat the `Ω(n log n)` comparison-sorting lower bound because they do **not** sort purely by comparisons.

## Counting sort

Use when keys are integers in a reasonably small range `[0..k]`.

Algorithm:

1. Count frequency of each key.
2. Convert counts to prefix sums (positions).
3. Place elements into output using positions.

Complexity:

- Time: `O(n + k)`
- Space: `O(n + k)` (output + counts)
- Stable: yes (when iterating input right-to-left during placement)

### When it is a bad idea

If `k` is huge (e.g., up to 10^9), `O(k)` space/time is not feasible.

## Radix sort (LSD)

Radix sort sorts by processing digits from least significant to most significant, using a **stable** subroutine (often counting sort).

For base `b` and `d` digits:

- Time: `O(d · (n + b))`
- Space: usually `O(n + b)`

Typical choices:

- Base 10 (decimal digits)
- Base 2^8 = 256 (bytes) for integers

## Key requirement: stability

For LSD radix sort to work, the per-digit sort must be **stable**, otherwise earlier digit ordering gets destroyed.

## Practical note

In high-level languages, radix sort is common inside optimized library implementations for integers/strings.
In interview settings, use it when:

- Keys have fixed width / limited digits
- `n` is large
- You want linear-ish time

