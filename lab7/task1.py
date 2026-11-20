from __future__ import annotations
from math import hypot, isfinite


class Rectangle:
    """Прямокутник із перевіркою розмірів та перевантаженням операцій."""

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    @staticmethod
    def is_valid(w: float, h: float) -> bool:
        return all(
            isinstance(v, (int, float)) and not isinstance(v, bool)
            and isfinite(v) and v > 0 for v in (w, h)
        )

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        if not self.is_valid(value, 1):
            raise ValueError('Ширина повинна бути додатним скінченним числом.')
        self._width = float(value)

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        if not self.is_valid(1, value):
            raise ValueError('Висота повинна бути додатним скінченним числом.')
        self._height = float(value)

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    @property
    def diagonal(self) -> float:
        return hypot(self.width, self.height)

    @property
    def is_square(self) -> bool:
        return self.width == self.height

    def scale(self, factor: float) -> Rectangle:
        if not self.is_valid(factor, 1):
            raise ValueError('Масштаб повинен бути додатним числом.')
        return Rectangle(self.width * factor, self.height * factor)

    def describe(self) -> str:
        return (f'Прямокутник {self.width:g} x {self.height:g}; '
                f'площа: {self.area:g}; периметр: {self.perimeter:g}; '
                f'діагональ: {self.diagonal:.2f}; квадрат: {self.is_square}')

    def __repr__(self) -> str:
        return f'Rectangle(width={self.width:g}, height={self.height:g})'

    def __str__(self) -> str:
        return self.describe()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented
        return (self.width, self.height) == (other.width, other.height)

    def __lt__(self, other: Rectangle) -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area < other.area

    def __add__(self, other: Rectangle) -> Rectangle:
        if not isinstance(other, Rectangle):
            return NotImplemented
        return Rectangle(self.width, (self.area + other.area) / self.width)

    @classmethod
    def from_string(cls, text: str) -> Rectangle:
        try:
            w, h = text.lower().split('x')
            return cls(float(w), float(h))
        except (ValueError, TypeError):
            raise ValueError('Використовуйте формат 4x5 з додатними розмірами.') from None


def main() -> None:
    r = Rectangle(4, 5)
    print('1. str:', str(r))
    print('2. repr:', repr(r))
    print('3. Ширина і висота:', r.width, r.height)
    print('4. Площа:', r.area)
    print('5. Периметр:', r.perimeter)
    print('6. Діагональ:', r.diagonal)
    print('7. Квадрат:', r.is_square, Rectangle(3, 3).is_square)
    print('8. Масштабування:', r.scale(2))
    print('9. Оригінал після масштабування:', r)
    print('10. Опис:', r.describe())
    print('11. Рівність:', r == Rectangle(4, 5))
    print('12. Різні розміри:', r == Rectangle(5, 4))
    print('13. Порівняння площ:', Rectangle(2, 3) < r)
    print('14. Додавання:', r + Rectangle(2, 3))
    print('15. Із рядка:', Rectangle.from_string('4x5'))
    print('16. Валідація:', Rectangle.is_valid(4, 5), Rectangle.is_valid(-1, 5))
    r.width, r.height = 6, 7
    print('17. Нові розміри:', r)
    print('18. Сортування:', sorted([r, Rectangle(1, 2), Rectangle(3, 4)]))
    try:
        r.width = 0
    except ValueError as error:
        print('19. Перевірка setter:', error)
    try:
        r.area = 100
    except AttributeError:
        print('20. area доступна лише для читання.')


if __name__ == '__main__':
    main()
