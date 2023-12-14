from build_better import BuildBetter as Builder

def test_circular():
    action_A = "build A"
    action_B = "build B"
    config = {
        "A": {"depends": ["B"], "rule": action_A},
        "B": {"depends": ["A"], "rule": action_B},
    }
    try:
        Builder().build(config)
        assert False, "should have exception"
    except ValueError:
        pass

def test_no_dep():
    action_A = "build A"
    action_B = "build B"
    config = {
        "A": {"depends": [], "rule": action_A},
        "B": {"depends": [], "rule": action_B},
    }
    assert Builder().build(config) == [action_A, action_B]
