import sys

from architecture import OPS, VMState
from vm_base import VirtualMachineBase

class VirtualMachineStep(VirtualMachineBase):
    def run(self):
        self.state = VMState.STEPPING
        while True:
            if self.state == VMState.STEPPING:
                self.interact(self.ip)
            if self.state == VMState.FINISHED:
                break
        instruction = self.ram[self.ip]
        self.ip += 1
        op, arg0, arg1 = self.decode(instruction)
        self.execute(op, arg0, arg1)

    def disassemble(self, addr, instruction):
        op, arg0, arg1 = self.decode(instruction)
        assert op in OPS_LOOKUP, f"Unknown op code {op} at {addr}"
        return f"{OPS_LOOKUP[op]} | {arg0} | {arg1}"
