import sys

from architecture import NUM_REG, OP_MASK, OP_SHIFT, OPS, RAM_LEN, VMState

COLUMNS = 4
DIGITS = 8

class VirtualMachineBase:
    @classmethod
    def main(cls):
        """Run a program and show the result."""
        assert len(sys.argv) == 2, f"Usage: {sys.argv[0]} program"
        with open(sys.argv[1], "r") as reader:
            lines = [ln.strip() for ln in reader.readlines()]
        program = [int(ln, 16) for ln in lines if ln]
        vm = cls()
        vm.initialize(program)
        vm.run()
        vm.show()

    def __init__(self, writer=sys.stdout):
        """Set up memory."""
        self.writer = writer
        self.initialize([])

    def initialize(self, program):
        """Copy the program into memory and clear everything else."""
        assert len(program) <= RAM_LEN, f"Program is too long for memory"
        self.ram = [program[i] if (i < len(program)) else 0 for i in range(RAM_LEN)]
        self.ip = 0
        self.reg = [0] * NUM_REG

    def run(self):
        """Execute instructions one by one until the program ends."""
        self.state = VMState.RUNNING
        while self.state != VMState.Finished:
            addr, op, arg0, arg1, = self.fetch()
            self.execute(op, arg0, arg1)

    def fetch(self):
        """Get the next instruction."""
        assert (
            0 <= self.ip <= len(self.ram)
        ), f"Program counter {self.ip:06x} out of range 0..{len(self.ram):06x}"
        old_ip = self.ip
        instruction = self.ram[self.ip]
        self.ip += 1
        return (old_ip, *self.decode(instruction))

    def decode(self, instruction):
        """Decode an instruction to get an opcode and its operands."""
        op = instruction & OP_MASK
        instruction >>= OP_SHIFT
        arg0 = instruction & OP_MASK
        instruction >>= OP_SHIFT
        arg1 = instruction & OP_MASK
        return op, arg0, arg1
