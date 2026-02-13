from project.dsa.edit_distance import levenshtein_distance


def test_levenshtein_distance_examples() -> None:
    assert levenshtein_distance("kitten", "sitting") == 3
    assert levenshtein_distance("flaw", "lawn") == 2


def test_levenshtein_distance_edge_cases() -> None:
    assert levenshtein_distance("", "") == 0
    assert levenshtein_distance("", "abc") == 3
    assert levenshtein_distance("abc", "") == 3
    assert levenshtein_distance("abc", "abc") == 0
