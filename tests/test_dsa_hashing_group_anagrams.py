import pytest

from project.dsa.hashing_group_anagrams import group_anagrams


def _as_sets(groups: list[list[str]]) -> set[frozenset[str]]:
    return {frozenset(g) for g in groups}


def test_group_anagrams_basic() -> None:
    inp = ["eat", "tea", "tan", "ate", "nat", "bat"]
    out = group_anagrams(inp)
    assert _as_sets(out) == {
        frozenset({"eat", "tea", "ate"}),
        frozenset({"tan", "nat"}),
        frozenset({"bat"}),
    }


def test_group_anagrams_empty() -> None:
    assert group_anagrams([]) == []


def test_group_anagrams_rejects_non_lowercase() -> None:
    with pytest.raises(ValueError):
        group_anagrams(["Tea"])
