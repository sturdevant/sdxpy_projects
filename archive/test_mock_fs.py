import pyfakefs
from pathlib import Path

def test_simple_example(fs):
    sentence = "This file contains one sentence."
    with open("alpha.txt", "w") as writer:
        writer.write(sentence)
    assert Path("alpha.txt").exists()
    with open("alpha.txt") as reader:
        assert reader.read() == sentence
