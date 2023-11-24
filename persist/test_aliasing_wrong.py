from io import StringIO

import pytest
from aliasing_wrong import LoadAlias, SaveAlias

def test_aliasing_no_aliasing():
    fixture = ["a", {"b": True, 7: {"c": "d"}}]
    assert roundtrip(fixture) == fixture

def roundtrip(fixture):
    writer = StringIO()
    SaveAlias(writer).save(fixture)
    reader = StringIO(writer.getvalue())
    return LoadAlias(reader).load()

def test_aliasing_shared_child():
    shared = ["content"]
    fixture = [shared, shared]
    result = roundtrip(fixture)
    assert result == fixture
    assert id(result[0]) == id(result[1])
    result[0][0] = "changed"
    assert result[1][0] == "changed"

def test_aliasing_circular():
    fixture = []
    fixture.append(fixture)
    result = roundtrip(fixture)
    assert len(result) == 1
    assert id(result) == id(result[0])
