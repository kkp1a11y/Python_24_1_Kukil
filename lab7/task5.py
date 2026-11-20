from __future__ import annotations
from abc import ABC, abstractmethod
from collections.abc import Iterator
from dataclasses import dataclass
from datetime import date
from math import isfinite
from typing import Any, ClassVar


@dataclass(frozen=True)
class Grade:
    """Оцінка з назвою дисципліни та датою виставлення."""

    subject: str
    value: float
    date: date

    def __post_init__(self) -> None:
        if not self.subject.strip() or not 0 <= self.value <= 5:
            raise ValueError('Потрібні назва дисципліни й оцінка від 0 до 5.')


class Person(ABC):
    """Абстрактна особа з унікальним ID та спільним реєстром."""

    __slots__ = ('name', 'email', '__id')
    _registry: ClassVar[list[Person]] = []
    _counter: ClassVar[int] = 0

    def __init__(self, *, name: str, email: str, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        if not name.strip() or '@' not in email:
            raise ValueError('Вкажіть ім’я та email із символом @.')
        self.name, self.email = name, email
        Person._counter += 1
        self.__id = f'PER-{Person._counter:03d}'
        Person._registry.append(self)

    @property
    def id(self) -> str:
        return self.__id

    @classmethod
    def get_registry(cls) -> tuple[Person, ...]:
        return tuple(Person._registry)

    @abstractmethod
    def role(self) -> str:
        pass

    @abstractmethod
    def contact_info(self) -> str:
        pass

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Person):
            return NotImplemented
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

    def __repr__(self) -> str:
        return f'{type(self).__name__}(id={self.id!r}, name={self.name!r})'


class Student(Person):
    """Студент зі списками оцінок та академічним статусом."""

    def __init__(self, *, year: int, major: str, **kwargs: Any) -> None:
        if type(year) is not int or not 1 <= year <= 6:
            raise ValueError('Рік навчання повинен бути від 1 до 6.')
        self.year, self.major = year, major
        self._grades: dict[str, list[float]] = {}
        self._grade_records: list[Grade] = []
        super().__init__(**kwargs)

    def role(self) -> str:
        return 'Студент'

    def contact_info(self) -> str:
        return f'{self.name}: {self.email}, спеціальність: {self.major}'

    def add_grade(self, subject: str, grade: float) -> None:
        record = Grade(subject.strip(), float(grade), date.today())
        self._grades.setdefault(record.subject, []).append(record.value)
        self._grade_records.append(record)

    @property
    def gpa(self) -> float:
        values = [g for grades in self._grades.values() for g in grades]
        return sum(values) / len(values) if values else 0.0

    @property
    def academic_status(self) -> str:
        if not self._grades:
            return 'немає оцінок'
        if self.gpa >= 4.5:
            return 'відмінник'
        if self.gpa >= 3.5:
            return 'хорошист'
        if self.gpa >= 3:
            return 'задовільно'
        return 'незадовільно'

    def transcript(self) -> str:
        lines = [f'{self.role()}: {self.name}; курс: {self.year}; {self.major}']
        for record in self._grade_records:
            lines.append(f'  {record.subject}: {record.value:g}, {record.date.isoformat()}')
        lines.append(f'  Середній бал: {self.gpa:.2f}; статус: {self.academic_status}')
        return '\n'.join(lines)


class Teacher(Person):
    """Викладач із зарплатою та переліком дисциплін."""

    def __init__(self, *, department: str, salary: float,
                 courses: list[str] | None = None, **kwargs: Any) -> None:
        self.department = department
        self.salary = salary
        self.courses = list(courses) if courses is not None else []
        super().__init__(**kwargs)

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        if not isfinite(value) or value < 0:
            raise ValueError('Зарплата повинна бути невід’ємним скінченним числом.')
        self._salary = float(value)

    @property
    def annual_salary(self) -> float:
        return self.salary * 12

    def assign_course(self, course: str) -> None:
        course = course.strip()
        if not course:
            raise ValueError('Назва дисципліни не може бути порожньою.')
        if course not in self.courses:
            self.courses.append(course)

    def remove_course(self, course: str) -> None:
        self.courses.remove(course)

    def role(self) -> str:
        return 'Викладач'

    def contact_info(self) -> str:
        return f'{self.name}: {self.email}, кафедра: {self.department}'


class GradStudent(Student, Teacher):
    """Аспірант, який поєднує навчання і викладацьку роботу."""

    def __init__(self, *, thesis_topic: str, supervisor: Teacher,
                 **kwargs: Any) -> None:
        self.thesis_topic, self.supervisor = thesis_topic, supervisor
        super().__init__(**kwargs)

    def role(self) -> str:
        return 'Аспірант'

    def contact_info(self) -> str:
        return (super().contact_info() + f'; кафедра: {self.department}; '
                f'керівник: {self.supervisor.name}')


class Department:
    """Кафедра з ітерацією по особах та обчисленням статистики."""

    def __init__(self, name: str, head: Teacher) -> None:
        if not isinstance(head, Teacher):
            raise TypeError('Завідувач повинен бути викладачем.')
        self.name, self.head = name, head
        self.members: list[Person] = []
        self.add_member(head)

    def add_member(self, person: Person) -> None:
        if not isinstance(person, Person):
            raise TypeError('Учасник повинен бути особою.')
        if person not in self.members:
            self.members.append(person)

    def remove_member(self, person: Person) -> None:
        if person == self.head:
            raise ValueError('Спочатку призначте іншого завідувача.')
        self.members.remove(person)

    def __iter__(self) -> Iterator[Person]:
        return iter(self.members)

    def average_student_gpa(self) -> float:
        students = [p for p in self.members if isinstance(p, Student)]
        return sum(p.gpa for p in students) / len(students) if students else 0.0

    def teacher_count(self) -> int:
        return sum(isinstance(p, Teacher) for p in self.members)

    def student_count(self) -> int:
        return sum(isinstance(p, Student) for p in self.members)

    def report(self) -> str:
        lines = [f'Кафедра: {self.name}', f'Завідувач: {self.head.name}']
        for person in self:
            lines.append(f'\n{person.id} | {person.role()} | {person.contact_info()}')
            if isinstance(person, Student):
                lines.append(person.transcript())
            if isinstance(person, Teacher):
                lines.append(f'  Дисципліни: {", ".join(person.courses) or "немає"}')
                lines.append(f'  Зарплата: {person.salary:.2f}; річна: {person.annual_salary:.2f}')
            if isinstance(person, GradStudent):
                lines.append(f'  Тема дисертації: {person.thesis_topic}')
        lines.append(f'\nСтудентських ролей: {self.student_count()}; '
                     f'викладацьких ролей: {self.teacher_count()}; '
                     f'середній бал: {self.average_student_gpa():.2f}')
        return '\n'.join(lines)


class University:
    """Університет із кафедрами, зарахуванням та пошуком осіб."""

    def __init__(self, name: str) -> None:
        self.name = name
        self._departments: dict[str, Department] = {}

    def add_department(self, department: Department) -> None:
        if department.name in self._departments:
            raise ValueError('Кафедра з такою назвою вже існує.')
        self._departments[department.name] = department

    def enroll_student(self, dept_name: str, student: Student) -> None:
        if not isinstance(student, Student):
            raise TypeError('Очікується студент.')
        self._departments[dept_name].add_member(student)

    def hire_teacher(self, dept_name: str, teacher: Teacher) -> None:
        if not isinstance(teacher, Teacher):
            raise TypeError('Очікується викладач.')
        if teacher.department != dept_name:
            raise ValueError('Кафедра викладача не відповідає вибраній.')
        self._departments[dept_name].add_member(teacher)

    def _people(self) -> set[Person]:
        return {p for dept in self._departments.values() for p in dept}

    def overall_stats(self) -> str:
        people = self._people()
        grads = sum(isinstance(p, GradStudent) for p in people)
        students = sum(isinstance(p, Student) for p in people)
        teachers = sum(isinstance(p, Teacher) for p in people)
        return (f'Університет: {self.name}\nКафедр: {len(self._departments)}\n'
                f'Унікальних осіб: {len(people)}\n'
                f'Студентів без аспірантів: {students - grads}\n'
                f'Викладачів без аспірантів: {teachers - grads}\n'
                f'Аспірантів: {grads}\n'
                f'Студентських ролей: {students}; викладацьких ролей: {teachers}')

    def find_person(self, name: str) -> list[Person]:
        return sorted((p for p in self._people() if p.name.casefold() == name.casefold()),
                      key=lambda p: p.id)

    def report(self) -> str:
        return '\n\n'.join([self.overall_stats()] + [d.report() for d in self._departments.values()])


def main() -> None:
    university = University('Житомирська політехніка')
    teachers = [
        Teacher(name='Олександр Коваль', email='koval@example.com',
                department='Інженерія ПЗ', salary=25000),
        Teacher(name='Наталія Мельник', email='melnyk@example.com',
                department='Інженерія ПЗ', salary=23000),
        Teacher(name='Ігор Бондар', email='bondar@example.com',
                department='Комп’ютерні науки', salary=26000),
        Teacher(name='Олена Мороз', email='moroz@example.com',
                department='Комп’ютерні науки', salary=24000),
    ]
    first = Department('Інженерія ПЗ', teachers[0])
    second = Department('Комп’ютерні науки', teachers[2])
    university.add_department(first)
    university.add_department(second)
    for teacher, course in zip(teachers, ['Python', 'Бази даних', 'Алгоритми', 'Мережі']):
        teacher.assign_course(course)
        university.hire_teacher(teacher.department, teacher)
    names = ['Костянтин Кукіль', 'Марія Шевченко', 'Андрій Ткаченко', 'Софія Кравчук',
             'Іван Лисенко', 'Наталія Олійник', 'Богдан Савченко', 'Катерина Петренко']
    for i, name in enumerate(names):
        dept = first if i < 4 else second
        student = Student(name=name, email=f'student{i + 1}@example.com',
                          year=3, major=dept.name)
        student.add_grade('Python', 5 if i % 2 == 0 else 4)
        student.add_grade('Математика', 4)
        university.enroll_student(dept.name, student)
    grad = GradStudent(name='Дмитро Романенко', email='grad@example.com',
                       year=1, major='Інженерія ПЗ', department=first.name, salary=15000,
                       thesis_topic='Автоматизоване тестування програм', supervisor=teachers[0])
    grad.add_grade('Методологія досліджень', 5)
    grad.assign_course('Практикум Python')
    university.enroll_student(first.name, grad)
    university.hire_teacher(first.name, grad)
    print(university.report())
    print('\n--- MRO ---')
    print(' -> '.join(cls.__name__ for cls in GradStudent.__mro__))
    print('\n--- Реєстр Person ---')
    for person in Person.get_registry():
        print(repr(person))
    print('Записів у реєстрі:', len(Person.get_registry()))
    print('Пошук:', university.find_person('Костянтин Кукіль'))
    print('Рівність:', grad == grad, grad == teachers[0])
    print('Множина з повтором аспіранта:', len({grad, grad}))
    teachers[0].assign_course('Тимчасовий курс')
    teachers[0].remove_course('Тимчасовий курс')
    first.remove_member(grad)
    first.add_member(grad)
    print('Після видалення й повернення аспіранта:', len(first.members))
    try:
        teachers[0].salary = -100
    except ValueError as error:
        print('Перевірка зарплати:', error)
    try:
        Person(name='Тест', email='test@example.com')
    except TypeError:
        print('Абстрактний клас Person не можна створити безпосередньо.')


if __name__ == '__main__':
    main()
