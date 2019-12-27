import pytest
from advent.y2019.intcode import Intcode, Mode

def test_simple_io_program():
    prog = [3,0,4,0,99]
    comp = Intcode(prog)
    comp.input(42)
    comp.run()    
    assert comp.output() == 42

def test_simple_io_program2():
    prog = [3,0,4,0,99]
    comp = Intcode(prog)
    comp.run()
    comp.input(42)
    comp.run()    
    assert comp.output() == 42

testdata = [
    [1, 1, [Mode(0), Mode(0), Mode(0)]],
    [1002, 2, [Mode(0), Mode(1), Mode(0)]],
    [21004, 4, [Mode(2), Mode(1), Mode(0)]]
]
@pytest.mark.parametrize("opcode,op_expected,mode_expected", testdata)
def test_parse_opcode(opcode, op_expected, mode_expected):
    (op, mode) = Intcode.parse_opcode(opcode)
    assert op == op_expected
    assert mode == mode_expected

def test_read_mode_program():
    prog = [1002,4,3,4,33]
    comp = Intcode(prog)
    comp.run()
    assert comp.program == [1002,4,3,4,99]

def test_negativ_values_program():
    prog = [1101,100,-1,4,0]
    comp = Intcode(prog)
    comp.run()
    assert comp.program == [1101,100,-1,4,99]

def test_part1():
    with open("input.txt", "r") as file:
        prog = Intcode.parse_prog(file.read())
        # print("prog", prog)
        comp = Intcode(prog)
        comp.input(1)
        comp.run()
        assert comp.outputs[-1] == 13087969

def test_part2():
    with open("input.txt", "r") as file:
        prog = Intcode.parse_prog(file.read())
        # print("prog", prog)
        comp = Intcode(prog)
        comp.input(5)
        comp.run()
        print(comp.outputs)
        assert comp.outputs[-1] == 14110739