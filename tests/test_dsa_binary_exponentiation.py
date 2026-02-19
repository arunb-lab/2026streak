import pytest

from project.dsa.binary_exponentiation import pow_int, pow_mod


def test_pow_int_basic() -> None:
    assert pow_int(2, 0) == 1
    assert pow_int(2, 10) == 1024
    assert pow_int(-2, 3) == -8


def test_pow_mod_basic() -> None:
    assert pow_mod(2, 10, 1_000_000_007) == 1024
    assert pow_mod(2, 10, 7) == pow(2, 10, 7)
    assert pow_mod(-2, 5, 13) == pow(-2, 5, 13)


def test_validation() -> None:
    with pytest.raises(ValueError):
        pow_int(2, -1)

    with pytest.raises(ValueError):
        pow_mod(2, -1, 7)

    with pytest.raises(ValueError):
        pow_mod(2, 10, 0)
