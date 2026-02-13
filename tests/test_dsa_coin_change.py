import pytest

from project.dsa.coin_change import coin_change_min_coins


def test_coin_change_min_coins() -> None:
    assert coin_change_min_coins([1, 2, 5], 11) == 3  # 5+5+1
    assert coin_change_min_coins([2], 3) is None
    assert coin_change_min_coins([2], 0) == 0


def test_coin_change_validation() -> None:
    with pytest.raises(ValueError):
        coin_change_min_coins([0, 1], 3)
    with pytest.raises(ValueError):
        coin_change_min_coins([1, 2], -1)
