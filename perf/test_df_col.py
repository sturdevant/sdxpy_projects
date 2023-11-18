from df_col import DfCol

def test_construct_with_two_pairs():
    df = DfCol(a=[1, 2], b=[3, 4])
    assert df.get("a", 0) == 1
    assert df.get("a", 1) == 2
    assert df.get("b", 0) == 3
    assert df.get("b", 1) == 4

def test_filter():
    def odd(a, b):
        return a % 2 == 1

    df = DfCol(a=[1, 2], b=[3, 4])
    assert df.filter(odd).eq(DfCol(a=[1], b=[3]))
