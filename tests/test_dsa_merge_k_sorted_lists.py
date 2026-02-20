from project.dsa.merge_k_sorted_lists import from_list, merge_k_lists, to_list


def test_merge_k_lists_basic() -> None:
    a = from_list([1, 4, 5])
    b = from_list([1, 3, 4])
    c = from_list([2, 6])

    out = merge_k_lists([a, b, c])
    assert to_list(out) == [1, 1, 2, 3, 4, 4, 5, 6]


def test_merge_k_lists_with_empty_lists() -> None:
    out = merge_k_lists([None, from_list([]), from_list([0])])
    assert to_list(out) == [0]


def test_merge_k_lists_all_empty() -> None:
    assert merge_k_lists([None, None]) is None
