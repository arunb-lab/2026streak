# Collision Resolution

A collision happens when two different keys map to the same bucket/slot.

## 1) Separate chaining

Each bucket stores a collection of items (often a linked list or dynamic array).

- Insert: compute bucket index, append to bucket
- Lookup: scan the bucket

Complexity (with uniform hashing):

- Expected bucket size ≈ load factor α
- Expected lookup time: `O(1 + α)`

Pros:

- Simple
- Deletion is straightforward

Cons:

- Extra memory for bucket structures

## 2) Open addressing

All items live inside the table array.
If a slot is taken, probe other slots in a deterministic sequence.

Common probing strategies:

- Linear probing: `i, i+1, i+2, ...`
- Quadratic probing
- Double hashing

Pros:

- No extra per-bucket allocations
- Better cache locality

Cons:

- Deletion needs tombstones
- Performance degrades quickly as α approaches 1

## Tiny illustrative implementation (chaining)

See: `DSA/notes/code/hash_table_chaining.py`

