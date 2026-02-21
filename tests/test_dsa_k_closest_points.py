from project.dsa.k_closest_points import k_closest


def _dist2(p: tuple[int, int]) -> int:
    return p[0] * p[0] + p[1] * p[1]


def test_k_closest_basic() -> None:
    pts = [(1, 3), (-2, 2), (2, -2), (5, 8)]
    r = k_closest(pts, 2)
    assert len(r) == 2
    # Returned order may vary; validate by distance.
    assert sorted(map(_dist2, r)) == sorted(map(_dist2, [(-2, 2), (2, -2)]))


def test_k_closest_k_zero() -> None:
    assert k_closest([(1, 1)], 0) == []
