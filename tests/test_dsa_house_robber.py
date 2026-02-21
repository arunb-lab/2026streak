from project.dsa.house_robber import house_robber


def test_house_robber_examples() -> None:
    assert house_robber([1, 2, 3, 1]) == 4
    assert house_robber([2, 7, 9, 3, 1]) == 12


def test_house_robber_edges() -> None:
    assert house_robber([]) == 0
    assert house_robber([5]) == 5
    assert house_robber([2, 1]) == 2
