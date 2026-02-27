from project.dsa.flood_fill import flood_fill


def test_flood_fill_basic() -> None:
    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1],
    ]
    assert flood_fill(image, 1, 1, 2) == [
        [2, 2, 2],
        [2, 2, 0],
        [2, 0, 1],
    ]


def test_flood_fill_noop_same_color() -> None:
    image = [[0, 0, 0], [0, 0, 0]]
    assert flood_fill(image, 0, 0, 0) == [[0, 0, 0], [0, 0, 0]]


def test_flood_fill_empty() -> None:
    assert flood_fill([], 0, 0, 1) == []
