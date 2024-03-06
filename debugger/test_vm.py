from assembler import Assembler
from vm_step import VirtualMachineStep as VM

class Writer:
    def __init__(self):
        self.seen = []

    def write(self, *args):
        self.seen.extend(args)
