# String Hashing & Rolling Hash

Hashing is turning a value into an integer “fingerprint”.

For strings, a common pattern is a **polynomial rolling hash**:

```
H(s) = (s[0]*p^0 + s[1]*p^1 + ... + s[n-1]*p^(n-1)) mod M
```

Where:

- `p` is a base (e.g., 31, 53, 911382323)
- `M` is a large modulus (often prime)

## Why rolling hash is useful

You can compute hashes for many substrings efficiently.

Precompute:

- prefix hashes
- powers of `p`

Then a substring hash can be computed in `O(1)`.

This enables pattern matching algorithms like **Rabin–Karp**:

- compare hashes first
- verify match to avoid false positives due to collisions

## Collisions

Different strings can have the same hash (pigeonhole principle).
Mitigations:

- use a large modulus
- use two moduli (double hashing)
- confirm equality after hash match

## Python example

See: `DSA/notes/code/rolling_hash.py`

