from project.dsa.aho_corasick import AhoCorasick


def test_aho_corasick_basic_matches() -> None:
    ac = AhoCorasick(["he", "she", "his", "hers"])
    spans = ac.find_spans("ahishers")

    # Validate existence of key matches (order may vary by traversal).
    assert (1, 4, "his") in spans
    assert (3, 5, "she") in spans
    assert (4, 6, "he") in spans
    assert (4, 8, "hers") in spans


def test_aho_corasick_empty_patterns_ok() -> None:
    ac = AhoCorasick([])
    assert ac.find_spans("abc") == []


def test_aho_corasick_overlapping_patterns() -> None:
    ac = AhoCorasick(["aa", "a"])
    spans = ac.find_spans("aaaa")
    # 'a' matches at 0..1,1..2,2..3,3..4
    assert spans.count((0, 1, "a")) == 1
    assert spans.count((3, 4, "a")) == 1
    # 'aa' matches at 0..2,1..3,2..4
    assert (0, 2, "aa") in spans
    assert (1, 3, "aa") in spans
    assert (2, 4, "aa") in spans
