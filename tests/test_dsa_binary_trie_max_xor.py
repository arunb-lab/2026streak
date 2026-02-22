import pytest

from project.dsa.binary_trie_max_xor import BinaryTrie, max_xor_pair


def test_max_xor_pair_examples() -> None:
    assert max_xor_pair([3, 10, 5, 25, 2, 8]) == 28  # 5 ^ 25
    assert max_xor_pair([0]) == 0
    assert max_xor_pair([]) == 0


def test_binary_trie_best_xor() -> None:
    t = BinaryTrie(bit_width=5)
    for x in [1, 2, 3, 7]:
        t.insert(x)

    assert t.best_xor(0) == 7
    assert t.best_xor(7) == 6  # 7 ^ 1 = 6


def test_binary_trie_validation() -> None:
    with pytest.raises(ValueError):
        BinaryTrie(bit_width=0)

    t = BinaryTrie()
    with pytest.raises(ValueError):
        t.best_xor(1)

    with pytest.raises(ValueError):
        t.insert(-1)
