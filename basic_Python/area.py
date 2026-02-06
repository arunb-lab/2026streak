from __future__ import annotations

import math


class Circle:
    """Circle helper used in basic OOP exercises."""

    def __init__(self, r: float) -> None:
        if r < 0:
            raise ValueError("radius must be non-negative")
        self.r = r

    def area(self) -> float:
        return math.pi * (self.r**2)


if __name__ == "__main__":
    ins = Circle(5)
    print("Area of the circle:", ins.area())
