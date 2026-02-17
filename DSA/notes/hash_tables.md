# Hash Tables

A **hash table** maps keys → buckets/slots using a hash function.

Most languages implement maps/sets using hash tables (Python: `dict` / `set`).

## Expected O(1)

With a good hash function and controlled **load factor**, operations are expected constant time:

- insert
- lookup
- delete

Why “expected”?

- It assumes keys distribute reasonably uniformly across buckets.

## Load factor (α)

Load factor:

- `α = (number of stored elements) / (number of buckets)`

As α grows, collisions grow.

Typical strategy:

- Keep α below a threshold (e.g., 0.66–0.9)
- When threshold exceeded, **resize** (often ×2) and rehash

This makes operations **amortized O(1)**.

## Collision handling

Two broad families:

1. **Separate chaining**
   - each bucket holds a small list (or a tree) of items
2. **Open addressing**
   - items stored in the table itself; probe to find a free slot

See [collision resolution](./collision_resolution.md).

## Worst-case O(n)

Worst-case happens if many keys collide into one bucket (or probe chains get long).
Real implementations mitigate:

- randomized hash seeds
- better hash functions
- switching buckets from list → balanced tree when long (in some languages)

