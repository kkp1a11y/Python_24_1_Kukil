from __future__ import annotations
from typing import ClassVar


class Student:
    """Студент із контрольованими властивостями та приватним номером."""

    _registry: ClassVar[dict[str, Student]] = {}
    _counter: ClassVar[int] = 0

    def __init__(self, name: str, year: int, gpa: float = 0.0) -> None:
        if not self.validate_name(name):
            raise ValueError("Ім'я повинно містити лише літери.")
        self.name = name
        self.year = year
        self.gpa = gpa
        self._courses: list[str] = []
        Student._counter += 1
        self.__student_id = f'STU-{Student._counter:03d}'
        Student._registry[self.__student_id] = self

    @staticmethod
    def validate_name(name: str) -> bool:
        return isinstance(name, str) and name.isalpha()

    @property
    def student_id(self) -> str:
        return self.__student_id

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int) -> None:
        if type(value) is not int or not 1 <= value <= 6:
            raise ValueError('Рік навчання повинен бути цілим числом від 1 до 6.')
        self._year = value

    @property
    def gpa(self) -> float:
        return self._gpa

    @gpa.setter
    def gpa(self, value: float) -> None:
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not 0 <= value <= 5:
            raise ValueError('Середній бал повинен бути від 0 до 5.')
        self._gpa = float(value)

    def add_course(self, name: str) -> None:
        name = name.strip()
        if not name:
            raise ValueError('Назва курсу не може бути порожньою.')
        if name not in self._courses:
            self._courses.append(name)

    def remove_course(self, name: str) -> None:
        if name not in self._courses:
            raise ValueError('Такого курсу немає у списку.')
        self._courses.remove(name)

    def get_transcript(self) -> str:
        courses = ', '.join(self._courses) or 'немає'
        return (f'Студент: {self.name}\nНомер: {self.student_id}\n'
                f'Рік: {self.year}\nСередній бал: {self.gpa:.2f}\nКурси: {courses}')

    @classmethod
    def get_count(cls) -> int:
        return len(cls._registry)

    @classmethod
    def find_by_id(cls, id: str) -> Student | None:
        return cls._registry.get(id)


def main() -> None:
    first = Student('Костянтин', 3, 4.5)
    second = Student('Олена', 2, 4.8)
    first.add_course('Python')
    first.add_course('Бази даних')
    first.add_course('Математика')
    first.remove_course('Математика')
    print('--- Відомість ---')
    print(first.get_transcript())
    print('\nPublic:', first.name, first.year)
    print('Protected доступний технічно:', first._gpa)
    try:
        print(first.__student_id)
    except AttributeError as error:
        print('Прямий доступ до private:', error)
    print('Правильний доступ через property:', first.student_id)
    first.year, first.gpa = 4, 4.9
    print('\nПісля зміни:\n' + first.get_transcript())
    print('\nКількість студентів:', Student.get_count())
    found = Student.find_by_id(second.student_id)
    print('Пошук за ID:', found.name if found else 'не знайдено')
    print('Невідомий ID:', Student.find_by_id('STU-999'))
    print('Перевірка імен:', Student.validate_name('Іван'), Student.validate_name('Іван123'))
    for field, value in [('year', 7), ('gpa', 6)]:
        try:
            setattr(first, field, value)
        except ValueError as error:
            print(f'Помилка {field}:', error)


if __name__ == '__main__':
    main()
