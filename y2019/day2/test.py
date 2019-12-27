import pytest
from advent.y2019.intcode import Intcode

testcases = [
    [[1,0,0,0,99],[2,0,0,0,99]],
    [[2,3,0,3,99],[2,3,0,6,99]],
    [[2,4,4,5,99,0],[2,4,4,5,99,9801]],
    [[1,1,1,4,99,5,6,0,99],[30,1,1,4,2,5,6,0,99]],
    [[1,9,10,3,2,3,11,0,99,30,40,50],[3500,9,10,70,2,3,11,0,99,30,40,50]]
]

@pytest.mark.parametrize("prog,out", testcases)
def test_program(prog, out):
    comp = Intcode(prog)
    comp.run()
    assert comp.program == out

def test_part1():
    with open("input.txt", "r") as file:
        # prog = [int(x) for x in file.read().split(",")]
        prog = Intcode.parse_prog(file.read())
        prog[1] = 12
        prog[2] = 2
        comp = Intcode(prog)
        comp.run()
        assert comp.program[0] == 3562672
