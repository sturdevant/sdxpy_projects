from naive_iterator import NaiveIterator

def gather(buffer):
    result = ""
    for char in buffer:
        result += char
    return result

def test_naive_buffer():
    buffer = NaiveIterator(["ab", "c"])
    assert gather(buffer) == "abc"

if __name__ == "__main__":
    test_naive_buffer()
