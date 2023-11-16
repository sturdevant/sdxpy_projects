from df_base import DataFrame
from util import dict_match

class DfRow(DataFrame):
    def __init__(self, rows):
        assert len(rows) > 0
        assert all(dict_match(r, rows[0]) for r in rows)
        self._data = rows

    def ncol(self):
        return len(self._data[0])

    def nrow(self):
        return len(self._data)

    def cols(self):
        return set(self._data[0].keys())

    def get(self, col, row):
        assert col in self._data[0]
        assert 0 <= row < len(self._data)
        return self._data[row][col]

    def eq(self, other):
        assert isinstance(other, DataFrame)
        for (i, row) in enumerate(self._data):
            for key in row:
                if key not in other.cols():
                    return False
                if row[key] != other.get(key, i):
                    return False
        return True

    def select(self, *names):
        assert all(n in self._data[0] for n in names)
        rows = [{key: r[key] for key in names} for r in self._data]
        return DfRow(rows)

    def filter(self, func):
        result = [r for r in self._data if func(**r)]
        return DfRow(result)
