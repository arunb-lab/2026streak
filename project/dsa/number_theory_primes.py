"""Prime utilities: sieve and prime factorization.

Includes:
- ``sieve(n)``: list of primes <= n.
- ``smallest_prime_factors(n)``: SPF table for 0..n.
- ``prime_factors(x, spf=None)``: factorization using optional SPF.

These are common building blocks for many number-theory / DSA problems.

Time complexity:
- sieve / spf: O(n log log n)
- factorization via spf: O(log x)
"""

from __future__ import annotations

from math import isqrt


def sieve(n: int) -> list[int]:
    """Return all primes p where 2 <= p <= n."""
    if n < 2:
        return []

    is_prime = bytearray(b"\x01") * (n + 1)
    is_prime[0:2] = b"\x00\x00"

    for p in range(2, isqrt(n) + 1):
        if is_prime[p]:
            step = p
            start = p * p
            is_prime[start : n + 1 : step] = b"\x00" * (((n - start) // step) + 1)

    return [i for i in range(2, n + 1) if is_prime[i]]


def smallest_prime_factors(n: int) -> list[int]:
    """Compute smallest prime factor (SPF) for every number in [0..n].

    For primes p, spf[p] == p. For composites, spf[x] is the smallest prime
    dividing x.

    Raises:
        ValueError: If n < 0.
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    spf = list(range(n + 1))
    if n >= 0:
        spf[0] = 0
    if n >= 1:
        spf[1] = 1

    for i in range(2, isqrt(n) + 1):
        if spf[i] == i:  # i is prime
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i

    return spf


def prime_factors(x: int, spf: list[int] | None = None) -> list[int]:
    """Return the prime factorization of ``x`` as a list of primes (with repeats).

    Args:
        x: Integer to factorize (must be >= 1).
        spf: Optional SPF table for faster factorization when x is small-ish.

    Examples:
        >>> prime_factors(72)
        [2, 2, 2, 3, 3]

    Raises:
        ValueError: If x < 1.
    """
    if x < 1:
        raise ValueError("x must be >= 1")

    if x in (0, 1):
        return []

    out: list[int] = []

    if spf is not None and x < len(spf):
        while x > 1:
            p = spf[x]
            out.append(p)
            x //= p
        return out

    # Fallback trial division.
    d = 2
    while d * d <= x:
        while x % d == 0:
            out.append(d)
            x //= d
        d += 1 if d == 2 else 2  # after 2, only odd candidates

    if x > 1:
        out.append(x)

    return out
