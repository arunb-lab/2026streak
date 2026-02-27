import pytest

from project.dsa.evaluate_rpn import eval_rpn


def test_eval_rpn_basic() -> None:
    assert eval_rpn(["2", "1", "+", "3", "*"]) == 9
    assert eval_rpn(["4", "13", "5", "/", "+"]) == 6


def test_eval_rpn_truncates_toward_zero() -> None:
    assert eval_rpn(["10", "3", "/"]) == 3
    assert eval_rpn(["-10", "3", "/"]) == -3


def test_eval_rpn_raises_on_malformed() -> None:
    with pytest.raises(ValueError):
        eval_rpn(["+"])

    with pytest.raises(ValueError):
        eval_rpn(["1", "2"])
