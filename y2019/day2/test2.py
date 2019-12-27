from advent.y2019.intcode import Intcode

def part2(prog):
    for noun in range(100):
        prog[1] = noun
        for verb in range(100):
            prog[2] = verb
            comp = Intcode(prog)
            comp.run()
            if comp.program[0] == 19690720:
                return 100 * noun + verb


def test_part2():
    with open("input.txt", "r") as file:
        prog = Intcode.parse_prog(file.read())
        result = part2(prog)
        assert result == 8250
