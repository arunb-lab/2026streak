# Python `dict` / `set` Complexity (and gotchas)

Python `dict` and `set` are hash tables.

## Typical complexity

For most workloads:

- membership (`x in s`): expected `O(1)`
- get/set/delete: expected `O(1)`
- iteration over all items: `O(n)`

The “expected” part assumes:

- a decent hash distribution
- table resizing keeps the load factor reasonable

## Worst-case complexity

Worst-case can degrade to `O(n)` per operation when many keys collide.

Python mitigations include:

- hash randomization for strings/bytes (harder to craft collision attacks)
- robust probing strategies (implementation detail)

But asymptotically, worst-case is still linear.

## Resizing and amortized costs

As you insert items, the table occasionally resizes and rehashes.
A single insert can trigger `O(n)` work, but across many inserts, average cost is **amortized `O(1)`**.

## Hashability rules

A key must be:

- hashable (`__hash__`)
- comparable for equality (`__eq__`) consistently

If you implement custom objects as keys:

- if you define `__eq__`, be careful to also define `__hash__` (or use `@dataclass(frozen=True)`)

## Common foot-guns

- Using a mutable object as a key (not allowed; e.g. list)
- Mutating an object used as a key (breaks lookup semantics)
- Assuming order is sorted (it is insertion-ordered since Python 3.7+, not sorted)

## Practical tips

- Prefer `set` for membership tests.
- Prefer `dict.get(key, default)` when missing keys are common.
- For counting: `collections.Counter` or `dict.setdefault` / `defaultdict(int)`.

