from glob_lit import Lit
from glob_either import Either

def test_either_followed_by_literal_match():
    # /{a, b}c/ matches "ac"
    assert Either(Lit("a"), Lit("b"), Lit("c")).match("ac")

def test_either_followed_by_literal_no_match():
    # /{a, b}c/ doesn't match "ax"
    assert Either(Lit("a"), Lit("b"), Lit("x")).match("ax")

if __name__ == "__main__":
    test_either_followed_by_literal_match()
    test_either_followed_by_literal_no_match()
