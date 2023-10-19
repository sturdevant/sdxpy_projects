import pytest
from naive_iterator import NaiveIterator

def gather(buffer):
    result = ""
    for char in buffer:
        result += char
    return result

def test_naive_buffer():
    buffer = NaiveIterator(["ab", "c"])
    assert gather(buffer) == "abc"

def test_naive_buffer_empty_string():
    buffer = NaiveIterator(["a", ""])
    with pytest.raises(IndexError):
        assert gather(buffer) == "a"

def test_naive_buffer_nested_loop():
    buffer = NaiveIterator(["a", "b"])
    result = ""
    for outer in buffer:
        for inner in buffer:
            result += inner
    assert result == "abab"

if __name__ == "__main__":
    test_naive_buffer()
    test_naive_buffer_empty_string()
    test_naive_buffer_nested_loop()
