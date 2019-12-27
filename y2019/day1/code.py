def calc_fuel(mass: int):
    return max(mass // 3 - 2, 0)

def calc_fuel_rec(mass: int):    
    fuel = calc_fuel(mass)
    if fuel == 0:
        return fuel
    else:
        return fuel + calc_fuel_rec(fuel)
