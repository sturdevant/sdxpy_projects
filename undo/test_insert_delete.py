from headless import HeadlessScreen
from insert_delete import InsertDeleteApp

def make_fixture(keys, size, lines):
    screen = HeadlessScreen(size, keys)
    app = InsertDeleteApp(size, lines)
    app(screen)
    return app

def test_delete_middle():
    app = make_fixture(["KEY_RIGHT", "DELETE"], (1, 3), ["abc"])
    assert app.get_log()[-1] == ("CONTROL_X", (0, 1), ["ac_"])

def test_delete_when_impossible():
    try:
        make_fixture(["DELETE"], (1, 1), [""])
    except AssertionError:
        pass
