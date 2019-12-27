import pytest
from code import calc_fuel, calc_fuel_rec

@pytest.mark.parametrize("mass,fuel", [[12, 2], [14, 2], [1969, 654], [100756, 33583]])
def test_calc_fuel(mass, fuel):
    assert calc_fuel(mass) == fuel

def test_calc_fuel_input_file():
    fuel = 0
    file = open('input.txt', 'r')
    for line in file:
        mass = int(line)
        fuel += calc_fuel(mass)
    assert fuel == 3443395

@pytest.mark.parametrize("mass,fuel", [[12, 2], [14, 2], [1969, 966], [100756, 50346]])
def test_calc_fuel_rec(mass, fuel):
    assert calc_fuel_rec(mass) == fuel

def test_calc_fuel_rec_input_file():
    fuel = 0
    file = open('input.txt', 'r')
    for line in file:
        mass = int(line)
        fuel += calc_fuel_rec(mass)
    assert fuel == 5162216
