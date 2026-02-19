import pytest

from project.dsa.number_theory_primes import (
    prime_factors,
    sieve,
    smallest_prime_factors,
)


def test_sieve_small() -> None:
    assert sieve(1) == []
    assert sieve(2) == [2]
    assert sieve(10) == [2, 3, 5, 7]


def test_spf_and_prime_factors() -> None:
    spf = smallest_prime_factors(100)

    assert spf[2] == 2
    assert spf[49] == 7
    assert prime_factors(72, spf=spf) == [2, 2, 2, 3, 3]
    assert prime_factors(97, spf=spf) == [97]


def test_prime_factors_validation_and_edges() -> None:
    with pytest.raises(ValueError):
        smallest_prime_factors(-1)

    with pytest.raises(ValueError):
        prime_factors(0)

    assert prime_factors(1) == []
