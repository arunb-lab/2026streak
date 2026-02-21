from project.dsa.minimum_size_subarray_sum import min_subarray_len


def test_min_subarray_len_examples() -> None:
    assert min_subarray_len(7, [2, 3, 1, 2, 4, 3]) == 2  # [4,3]
    assert min_subarray_len(4, [1, 4, 4]) == 1
    assert min_subarray_len(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0


def test_min_subarray_len_single_element() -> None:
    assert min_subarray_len(3, [3]) == 1
    assert min_subarray_len(4, [3]) == 0
