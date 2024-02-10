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
    
    def _find_labels(self, lines):
        result = {}
        loc = 0
        for ln in lines:
            if self._is_label(ln):
                label = ln[:-1].strip()
                assert label not in result, f"Duplicated {label}"
                result[label] = loc
            else:
                loc += 1
        return result

    def _is_label(self, line):
        return line.endswith(":")
