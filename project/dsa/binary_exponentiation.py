"""Binary Exponentiation (Fast Power).

Compute a^b quickly using exponentiation by squaring.

Includes:
- ``pow_int(a, b)`` for integer exponent b >= 0.
- ``pow_mod(a, b, mod)`` for modular exponentiation.

Time complexity: O(log b)
"""

from __future__ import annotations


def pow_int(a: int, b: int) -> int:
    """Return a**b for b >= 0 using fast exponentiation."""
    if b < 0:
        raise ValueError("exponent b must be non-negative")

    res = 1
    base = a
    exp = b

    while exp:
        if exp & 1:
            res *= base
        base *= base
        exp >>= 1

    return res


def pow_mod(a: int, b: int, mod: int) -> int:
    """Return (a**b) % mod for b >= 0.

    Raises:
        ValueError: If b < 0 or mod <= 0.
    """
    if b < 0:
        raise ValueError("exponent b must be non-negative")
    if mod <= 0:
        raise ValueError("mod must be positive")

    res = 1 % mod
    base = a % mod
    exp = b

    while exp:
        if exp & 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp >>= 1

    return res
