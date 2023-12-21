from z3 import sat, unsat, Bool, Solver

A = Bool("A")
B = Bool("B")
C = Bool("C")

def report(title, result):
    print(f"{title}: {result}")
    if result == sat:
        model = solver.model()
        for term in model:
            print(term, model[term])

solver = Solver()
solver.add(A == B)
solver.add(B == C)
report("A == B & B == C", solver.check())
