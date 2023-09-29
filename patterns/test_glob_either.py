from glob_lit import Lit
from glob_either import Either

def test_either_two_literals_first():
    # /{a, b}/ matches "a"
    assert Either(Lit("a"), Lit("b")).match("a")

def test_either_two_literals_not_both():
    # /{a, b}/ doesn't match "ab"
    assert not Either(Lit("a"), Lit("b")).match("ab")

if __name__ == "__main__":
    test_either_two_literals_first()
    test_either_two_literals_not_both()
