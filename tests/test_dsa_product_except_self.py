from project.dsa.product_except_self import product_except_self


def test_product_except_self_basic() -> None:
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]


def test_product_except_self_with_zero() -> None:
    assert product_except_self([1, 2, 0, 4]) == [0, 0, 8, 0]
    assert product_except_self([0, 0, 3]) == [0, 0, 0]


def test_product_except_self_edge_cases() -> None:
    assert product_except_self([]) == []
    assert product_except_self([5]) == [1]
