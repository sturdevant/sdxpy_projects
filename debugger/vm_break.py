import sys

from architecture import OPS, VMState
from vm_extend import VirtualMachineExtend

class VirtualMachineBreak(VirtualMachineExtend):
    def __init__(self):
        super().__init__()
        self.breaks = {}
        self.handlers |= {
            "b": self._do_add_breakpoint,
            "break": self._do_add_breakpoint,
            "c": self._do_clear_breakpoint,
            "clear": self._do_clear_breakpoint,
        }

    def show(self):
        super().show()
        if self.breaks:
            self.write("-" * 6)
            for key, instruction in self.breaks.items():
                self.write(f"{key:06x}: {self.disassemble(key, instruction)}")

    def _do_add_breakpoint(self, addr):
        if self.ram[addr] == OPS["brk"]["code"]:
            return True
        self.breaks[addr] = self.ram[addr]
        self.ram[addr] = OPS["brk"]["code"]
        return True

    def _do_clear_breakpoint(self, addr):
        if self.ram[addr] != OPS["brk"]["code"]:
            return True
        self.ram[addr] = self.breaks[addr]
        del self.breaks[addr]
        return True
