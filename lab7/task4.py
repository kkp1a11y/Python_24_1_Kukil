from __future__ import annotations
from collections.abc import Iterator


class Matrix:
    """Матриця з арифметичними операціями, індексацією та ітерацією."""

    def __init__(self, rows: int, cols: int,
                 data: list[list[float]] | None = None) -> None:
        if type(rows) is not int or type(cols) is not int or rows <= 0 or cols <= 0:
            raise ValueError('Розміри повинні бути додатними цілими числами.')
        self._rows, self._cols = rows, cols
        if data is None:
            self._data = [[0.0 for _ in range(cols)] for _ in range(rows)]
        else:
            if len(data) != rows or any(len(row) != cols for row in data):
                raise ValueError('Розміри data не відповідають rows і cols.')
            self._data = [[float(value) for value in row] for row in data]

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def cols(self) -> int:
        return self._cols

    @property
    def is_square(self) -> bool:
        return self.rows == self.cols

    @property
    def trace(self) -> float:
        if not self.is_square:
            raise ValueError('Слід визначений лише для квадратної матриці.')
        return sum(self._data[i][i] for i in range(self.rows))

    def __repr__(self) -> str:
        return f'Matrix({self.rows}, {self.cols}, {self._data!r})'

    def __str__(self) -> str:
        width = max(len(f'{v:g}') for row in self._data for v in row)
        return '\n'.join(' '.join(f'{v:>{width}g}' for v in row) for row in self._data)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Matrix):
            return NotImplemented
        return self._data == other._data

    def _same_size(self, other: Matrix) -> None:
        if (self.rows, self.cols) != (other.rows, other.cols):
            raise ValueError('Розміри матриць повинні збігатися.')

    def __add__(self, other: Matrix) -> Matrix:
        if not isinstance(other, Matrix):
            return NotImplemented
        self._same_size(other)
        return Matrix(self.rows, self.cols, [
            [self[i, j] + other[i, j] for j in range(self.cols)]
            for i in range(self.rows)
        ])

    def __sub__(self, other: Matrix) -> Matrix:
        if not isinstance(other, Matrix):
            return NotImplemented
        self._same_size(other)
        return Matrix(self.rows, self.cols, [
            [self[i, j] - other[i, j] for j in range(self.cols)]
            for i in range(self.rows)
        ])

    def __mul__(self, scalar: float) -> Matrix:
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Matrix(self.rows, self.cols, [
            [value * scalar for value in row] for row in self._data
        ])

    def __rmul__(self, scalar: float) -> Matrix:
        return self * scalar

    def __matmul__(self, other: Matrix) -> Matrix:
        if not isinstance(other, Matrix):
            return NotImplemented
        if self.cols != other.rows:
            raise ValueError('Для A @ B кількість стовпців A має дорівнювати рядкам B.')
        return Matrix(self.rows, other.cols, [
            [sum(self[i, k] * other[k, j] for k in range(self.cols))
             for j in range(other.cols)] for i in range(self.rows)
        ])

    def _check_key(self, key: tuple[int, int]) -> None:
        if not isinstance(key, tuple) or len(key) != 2:
            raise TypeError('Індекс повинен бути кортежем (i, j).')
        i, j = key
        if type(i) is not int or type(j) is not int:
            raise TypeError('Індекси повинні бути цілими числами.')
        if not (0 <= i < self.rows and 0 <= j < self.cols):
            raise IndexError('Індекс виходить за межі матриці.')

    def __getitem__(self, key: tuple[int, int]) -> float:
        self._check_key(key)
        return self._data[key[0]][key[1]]

    def __setitem__(self, key: tuple[int, int], value: float) -> None:
        self._check_key(key)
        self._data[key[0]][key[1]] = float(value)

    def __iter__(self) -> Iterator[list[float]]:
        for row in self._data:
            yield row.copy()

    def __len__(self) -> int:
        return self.rows

    def transpose(self) -> Matrix:
        return Matrix(self.cols, self.rows, [
            [self[i, j] for i in range(self.rows)] for j in range(self.cols)
        ])

    @classmethod
    def identity(cls, n: int) -> Matrix:
        result = cls(n, n)
        for i in range(n):
            result[i, i] = 1
        return result


def main() -> None:
    a = Matrix(2, 2, [[1, 2], [3, 4]])
    b = Matrix(2, 2, [[5, 6], [7, 8]])
    print('A:\n', a, sep='')
    print('B:\n', b, sep='')
    print('repr:', repr(a))
    print('Нульова матриця:\n', Matrix(2, 3), sep='')
    print('A + B:\n', a + b, sep='')
    print('A - B:\n', a - b, sep='')
    print('A * 2:\n', a * 2, sep='')
    print('3 * A:\n', 3 * a, sep='')
    print('A @ B:\n', a @ b, sep='')
    print('A == B:', a == b)
    print('A == копія A:', a == Matrix(2, 2, [[1, 2], [3, 4]]))
    print('rows, cols, is_square, trace:', a.rows, a.cols, a.is_square, a.trace)
    print('Транспонування:\n', a.transpose(), sep='')
    print('Одинична матриця:\n', Matrix.identity(3), sep='')
    print('A[0, 1]:', a[0, 1])
    a[0, 1] = 5
    print('Після A[0, 1] = 5:\n', a, sep='')
    print('len(A):', len(a))
    print('Ітерація по рядках:')
    for row in a:
        print(row)
    for action in [lambda: a + Matrix(3, 2), lambda: a @ Matrix(3, 2),
                   lambda: a[9, 0], lambda: Matrix(2, 3).trace]:
        try:
            action()
        except (ValueError, IndexError) as error:
            print('Перевірка помилки:', error)


if __name__ == '__main__':
    main()
