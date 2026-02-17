# Amortized Analysis

**Amortized** complexity spreads the cost of occasional expensive operations across many cheap ones.

It answers: “Over a long sequence of operations, what is the average cost per operation?”

## Dynamic array append (classic example)

Consider an array-backed list that grows by **doubling capacity**:

- Most `append(x)` operations just write into the next slot: `O(1)`.
- When the array is full, we allocate a new array (size ~2×) and copy all elements: `O(n)`.

### Why amortized `O(1)`?

Suppose capacities go: 1, 2, 4, 8, ...

Total number of element copies up to `n` appends:

- Copy 1 + 2 + 4 + ... + n/2 = `O(n)`.

So across `n` appends:

- Total work = `O(n)` (writes) + `O(n)` (copies) = `O(n)`
- Amortized per append = `O(n) / n = O(1)`

### Important nuance

Amortized `O(1)` does **not** mean each individual operation is `O(1)`.
It means the *average over a sequence* is constant.

## Hash tables: expected vs amortized

Hash tables often combine:

- **Expected `O(1)`** per operation assuming a good hash distribution.
- **Amortized `O(1)`** due to periodic resizing/rehashing.

A resize might cost `O(n)` to rehash all items, but it happens infrequently.

## Three common techniques

1. **Aggregate analysis**
   - Bound total cost of a sequence, divide by operations.

2. **Accounting method**
   - Charge cheap operations slightly more; save “credits” to pay for expensive ones.

3. **Potential method**
   - Define a potential function Φ(state) that tracks stored work.

For interviews / problem solving, aggregate analysis is usually enough.

## When amortized analysis matters

- Dynamic arrays / stacks
- Hash tables with resizing
- Union-Find (Disjoint Set Union) with path compression: almost constant (inverse Ackermann)

