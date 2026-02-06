import math

import pytest

from basic_Python.area import Circle


def test_circle_area_radius_5() -> None:
    c = Circle(5)
    assert c.area() == pytest.approx(math.pi * 25)


def test_circle_area_zero() -> None:
    c = Circle(0)
    assert c.area() == 0


def test_circle_negative_radius_raises() -> None:
    with pytest.raises(ValueError):
        Circle(-1)
