from architecture import RAM_LEN
from assembler import Assembler, main

class DataAllocator(Assembler):
    DIVIDER = ".data"

    def assemble(self, lines):
        lines = self._get_lines(lines)
        to_compile, to_allocate = self._split(lines)

        labels = self._find_labels(lines)
        instructions = [ln for ln in lines if not self._is_label(ln)]

        base_of_data = len(instructions)
        self._add_allocations(base_of_data, labels, to_allocate)

        compiled = [self._compile(instr, labels) for instr in instructions]
        program = self._to_text(compiled)
        return program
