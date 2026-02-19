"""Extended Euclidean Algorithm.

Provides:
- ``egcd(a, b)`` returning (g, x, y) s.t. ax + by = g = gcd(a, b).
- ``modinv(a, m)`` returning modular inverse of a modulo m, if it exists.

Time complexity: O(log min(a,b)).
"""

from __future__ import annotations


def egcd(a: int, b: int) -> tuple[int, int, int]:
    """Return (g, x, y) such that a*x + b*y = g = gcd(a,b)."""
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    g = abs(old_r)
    x, y = old_s, old_t

    # Normalize sign so g is non-negative and identity holds.
    if old_r < 0:
        x, y = -x, -y

    return g, x, y


def modinv(a: int, m: int) -> int | None:
    """Return modular inverse of ``a`` modulo ``m`` if it exists.

    Returns None when gcd(a, m) != 1.

    Raises:
        ValueError: If m <= 0.
    """
    if m <= 0:
        raise ValueError("modulus m must be positive")

    g, x, _ = egcd(a, m)
    if g != 1:
        return None
    return x % m
