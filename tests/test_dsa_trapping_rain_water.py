from project.dsa.trapping_rain_water import trap_rain_water


def test_trap_rain_water_examples() -> None:
    assert trap_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert trap_rain_water([4, 2, 0, 3, 2, 5]) == 9


def test_trap_rain_water_edges() -> None:
    assert trap_rain_water([]) == 0
    assert trap_rain_water([1]) == 0
    assert trap_rain_water([1, 2]) == 0
