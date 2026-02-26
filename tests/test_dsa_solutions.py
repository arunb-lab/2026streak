from __future__ import annotations

import runpy
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def load_fn(rel_path: str, fn_name: str):
    mod = runpy.run_path(str(REPO_ROOT / rel_path))
    return mod[fn_name]


def test_max_subarray():
    max_subarray = load_fn("DSA/arrays/02_maximum_subarray.py", "max_subarray")
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([1]) == 1


def test_two_sum():
    two_sum = load_fn("DSA/arrays/14_two_sum.py", "two_sum")
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)


def test_valid_parentheses():
    is_valid_parentheses = load_fn(
        "DSA/stack/01_valid_parentheses.py", "is_valid_parentheses"
    )
    assert is_valid_parentheses("()[]{}") is True
    assert is_valid_parentheses("([)]") is False


def test_coin_change_min_coins():
    coin_change_min_coins = load_fn("DSA/dp/01_coin_change.py", "coin_change_min_coins")
    assert coin_change_min_coins([1, 2, 5], 11) == 3
    assert coin_change_min_coins([2], 3) == -1
