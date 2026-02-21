from project.dsa.single_number_xor import single_number


def test_single_number_examples() -> None:
    assert single_number([2, 2, 1]) == 1
    assert single_number([4, 1, 2, 1, 2]) == 4
    assert single_number([1]) == 1
