from project.dsa.trie import Trie


def test_trie_insert_contains_prefix() -> None:
    t = Trie()
    assert t.contains("a") is False

    t.insert("apple")
    assert t.contains("apple") is True
    assert t.contains("app") is False
    assert t.starts_with("app") is True

    t.insert("app")
    assert t.contains("app") is True


def test_trie_empty_string() -> None:
    t = Trie()
    assert t.contains("") is False
    t.insert("")
    assert t.contains("") is True
    assert t.starts_with("") is True
