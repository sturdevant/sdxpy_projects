import sys

from architecture import VMState
from vm_step import VirtualMachineStep

class VirtualMachineExtend(VirtualMachineStep):
    def _do_disassemble(self, addr):
        self.write(self.disassemble(addr, self.ram[addr]))
        return True

    def _do_ip(self, addr):
        self.write(f"{self.ip:06x}")
        return True

    def _do_memory(self, addr):
        self.show()
        return True

    def _do_quit(self, addr):
        self.state = VMState.FINISHED
        return False

    def _do_run(self, addr):
        self.state = VMState.RUNNING
        return False

    def _do_step(self, addr):
        self.state = VMState.STEPPING
        return False
