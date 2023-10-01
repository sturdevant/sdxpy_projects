from tokenizer import Tokenizer

def test_tok_empty_string():
    assert Tokenizer().tok("") == []

def test_tok_any_either():
    assert Tokenizer().tok("*{abc,def}") == [
            ["Any"],
            ["EitherStart"],
            ["Lit", "abc"],
            ["Lit", "def"],
            ["EitherEnd"],
        ]

if __name__ == "__main__":
    test_tok_empty_string()
    test_tok_any_either()
