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
