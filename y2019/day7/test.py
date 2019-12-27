from itertools import permutations
import pytest
from advent.y2019.intcode import Intcode

def part1():
    with open("input.txt", "r") as file:
        prog = Intcode.parse_prog(file.read())

        return max_amp(prog)

def part2():
    with open("input.txt", "r") as file:
        prog = Intcode.parse_prog(file.read())

        return max_amp_loop(prog)

def max_amp(prog: [int]):
    return max(amp(prog, perm, 0) for perm in permutations(range(5)))

def amp(prog: [int], perm: [int], value: int):
    for p in perm:
        comp = Intcode(prog)
        comp.input(p)
        comp.input(value)
        comp.run()
        value = comp.output()
    return value

testcases = [
    [[3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0], 43210],
    [[3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0], 54321],
    [[3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0], 65210]
]

@pytest.mark.parametrize("prog, expected", testcases)
def test_max_amp(prog, expected):
    assert max_amp(prog) == expected

def test_part1():
    assert part1() == 79723

def max_amp_loop(prog):
    return max(amp_loop(prog, perm, 0) for perm in permutations(range(5, 10)))

def amp_loop(prog: [int], perm: [int], value: int):
    comp = list(Intcode(prog) for _ in perm)
    for i, p in enumerate(perm):
        comp[i].input(p)

    i = 0
    while True:        
        c = comp[i % len(comp)]
        if (c.done): break
        c.input(value)
        c.run()
        value = c.output()
        # print(i, c.done)
        i += 1
    return comp[-1].outputs[-1]

testcases = [
    [[3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5], 139629729],
    [[3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10], 18216]
]

@pytest.mark.parametrize("prog, expected", testcases)
def test_max_amp_loop(prog, expected):
    assert max_amp_loop(prog) == expected

def test_part2():
    assert part2() == 70602018
