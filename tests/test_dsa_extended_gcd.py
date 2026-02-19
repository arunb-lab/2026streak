import pytest

from project.dsa.extended_gcd import egcd, modinv


def test_egcd_identity() -> None:
    g, x, y = egcd(240, 46)
    assert g == 2
    assert 240 * x + 46 * y == g


def test_modinv_exists() -> None:
    inv = modinv(3, 11)
    assert inv is not None
    assert (3 * inv) % 11 == 1


def test_modinv_none_when_not_coprime() -> None:
    assert modinv(6, 9) is None


def test_modinv_validation() -> None:
    with pytest.raises(ValueError):
        modinv(1, 0)
