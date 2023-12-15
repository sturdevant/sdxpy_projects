from build_time import BuildTime as Builder

def test_diamond_dep():
    action_A = "build A"
    action_B = "build B"
    action_C = "build C"
    action_D = "build D"
    config = {
        "A": {"depends": ["B", "C"], "rule": action_A, "time": 0},
        "B": {"depends": ["D"], "rule": action_B, "time": 0},
        "C": {"depends": ["D"], "rule": action_C, "time": 1},
        "D": {"depends": [], "rule": action_D, "time": 1},
    }
    assert Builder().build(config) == [action_B, action_A]
