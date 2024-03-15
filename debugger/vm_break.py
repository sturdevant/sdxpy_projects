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
