import sys
from architecture import NUM_REG, OP_SHIFT, OPS

class Assembler:
    def assemble(self, lines):
        lines = self._get_lines(lines)
        labels = self._find_labels(lines)
        instructions = [
            ln for ln in lines if not self._is_label(ln)
        ]
        compiled = [
            self._compile(instr, labels) for instr in instructions
        ]
        program = self._to_text(compiled)
        return program
