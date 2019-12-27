import enum

class Mode(enum.Enum):
    position = 0
    immediate = 1
    relative = 2

class Intcode:
    def __init__(self, program: [int], debug = False):
        self.program = list(program)
        self.p = 0

        self.inputs = []
        self.i = 0

        self.outputs = []
        self.o = 0

        self.relative = 0
        self.ready = True
        self.done = False        
        self.debug = debug
    
    def run(self):
        while (self.ready):
            self.step()
    
    def step(self):
        opcode = self.read(Mode.immediate)
        (op, mode) = Intcode.parse_opcode(opcode)
        # print("step", op, mode)
        self.exec(op, mode)

    def exec(self, op: int, mode: [int]):
        if op == 1:
            if self.debug: print("  exec: add")
            value = self.read(mode.pop()) + self.read(mode.pop())
            self.write(value, mode.pop())
        elif op == 2:
            if self.debug: print("  exec: multi")
            value = self.read(mode.pop()) * self.read(mode.pop())
            self.write(value, mode.pop())
        elif op == 3:
            if self.debug: print("  exec: input")
            if (self.i < len(self.inputs)):
                value = self.inputs[self.i]
                self.write(value, mode.pop())
                self.i += 1
            else:
                self.ready = False
                self.p -= 1
        elif op == 4:
            if self.debug: print("  exec: output")
            value = self.read(mode.pop())
            self.outputs.append(value)
        elif op == 5:
            if self.debug: print("  exec: jump-if-true")
            value = self.read(mode.pop())
            addr = self.read(mode.pop())
            if value != 0:
                self.p = addr
        elif op == 6:
            if self.debug: print("  exec: jump-if-false")
            value = self.read(mode.pop())
            addr = self.read(mode.pop())
            if value == 0:
                self.p = addr
        elif op == 7:
            if self.debug: print("  exec: less-than")
            a = self.read(mode.pop())
            b = self.read(mode.pop())
            value = 1 if a < b else 0
            self.write(value, mode.pop())
        elif op == 8:
            if self.debug: print("  exec: equal-to")
            a = self.read(mode.pop())
            b = self.read(mode.pop())
            value = 1 if a == b else 0
            self.write(value, mode.pop())
        elif op == 99:
            if self.debug: print("  exec: terminate")
            self.ready = False
            self.done = True
        else:
            raise ValueError("Unknown op", op)

    @staticmethod
    def parse_opcode(opcode: int):
        op = opcode % 100
        mode = [Mode(int(x)) for x in str(opcode // 100).rjust(3, '0')]
        return (op, mode)
    
    @staticmethod
    def parse_prog(prog: str):
        return [int(x) for x in prog.split(",")]

    def read(self, mode = Mode.position) -> int:
        # print("read", mode)
        if mode == Mode.position:
            value = self.program[self.program[self.p]]
        elif mode == Mode.immediate:
            value = self.program[self.p]
        elif mode == Mode.relative:
            value = self.program[self.relative + self.p]
        else:
            raise ValueError("Mode unknown", mode)

        self.p += 1

        return value

    def write(self, value, mode):
        addr = self.read(Mode.immediate)
        self.program[addr] = value

    def input(self, value: int):
        self.inputs.append(value)
        self.ready = True

    def output(self):
        value = self.outputs[self.o]
        self.o += 1
        return value