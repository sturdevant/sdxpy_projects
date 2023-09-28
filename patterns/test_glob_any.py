from glob_lit import Lit
from glob_any import Any

def test_any_matches_empty():
    # /*/ matches ""
    assert Any().match("")

def test_any_matches_entire_string():
    # /*/ matches "abc"
    assert Any().match("abc")

def test_any_matches_as_prefix():
    # /*def/ matches "abcdef"
    assert Any(Lit("def")).match("abcdef")

def test_any_matches_as_suffix():
    # /abc*/ matches "abcdef"
    assert Lit("abc", Any()).match("abcdef")

def test_any_matches_interior():
    # /a*c/ matches "abc"
    assert Lit("a", Any(Lit("c"))).match("abc")

if __name__ == "__main__":
    test_any_matches_empty()
    test_any_matches_entire_string()
    test_any_matches_as_prefix()
    test_any_matches_as_suffix()
    test_any_matches_interior()
