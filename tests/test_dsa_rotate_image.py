from project.dsa.rotate_image import rotate_image


def test_rotate_image_3x3() -> None:
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    rotate_image(m)
    assert m == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]


def test_rotate_image_1x1() -> None:
    m = [[42]]
    rotate_image(m)
    assert m == [[42]]
