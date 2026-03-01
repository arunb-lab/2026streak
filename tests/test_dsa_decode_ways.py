from project.dsa.decode_ways import decode_ways


def test_decode_ways_examples() -> None:
    assert decode_ways("12") == 2  # AB, L
    assert decode_ways("226") == 3  # BZ, VF, BBF
    assert decode_ways("06") == 0


def test_decode_ways_edge_cases() -> None:
    assert decode_ways("") == 0
    assert decode_ways("0") == 0
    assert decode_ways("10") == 1
    assert decode_ways("101") == 1
    assert decode_ways("100") == 0
