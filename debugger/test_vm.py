from assembler import Assembler
from vm_step import VirtualMachineStep as VM

class Reader:
    def __init__(self, *args):
        self.commands = args
        self.index = 0

    def __call__(self, prompt):
        assert self.index < len(self.commands)
        self.index += 1
        return self.commands[self.index - 1]

class Writer:
    def __init__(self):
        self.seen = []

    def write(self, *args):
        self.seen.extend(args)

def execute(source, reader, writer):
    program = Assembler().assemble(source.split("\n"), False)
    vm = VM(reader, writer)
    vm.initialize(program)
    vm.run()

def test_disassemble():
    source = """
    hlt
    """
    reader = Reader("d", "q")
    writer = Writer()
    execute(source, reader, writer)
    assert writer.seen == ["hlt | 0 | 0\n"]
