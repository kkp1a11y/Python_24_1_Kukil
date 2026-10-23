def add_student(students, name, year, gpa, courses):
    new_id = f'ST-{len(students) + 1:03d}'
    students[new_id] = (name, year, gpa, frozenset(courses))
    return new_id

def find_by_name(students, name):
    for sid, data in students.items():
        if data[0] == name:
            return sid, data
    return None

def top_students(students, n=3):
    pairs = [(data[0], data[2]) for data in students.values()]
    return sorted(pairs, key=lambda p: p[1], reverse=True)[:n]

def students_in_course(students, course_name):
    return {data[0] for data in students.values() if course_name in data[3]}

def common_courses(students, id1, id2):
    return students[id1][3] & students[id2][3]

def stats(students):
    all_courses = set()
    for data in students.values():
        all_courses |= data[3]
    return {
        'total': len(students),
        'avg_gpa': round(sum(d[2] for d in students.values()) / len(students), 2),
        'unique_courses': all_courses,
    }

students = {}
add_student(students, 'Іван',   2, 4.2, ['Python', 'Математика', 'Фізика'])
add_student(students, 'Марія',  3, 4.8, ['AI', 'Python', 'Статистика'])
add_student(students, 'Олег',   1, 3.5, ['Python'])
add_student(students, 'Анна',   2, 4.5, ['Python', 'Математика', 'Фізика'])
add_student(students, 'Денис',  4, 3.9, ['AI', 'Статистика', 'Бази даних'])
add_student(students, 'Софія',  3, 4.7, ['AI', 'Python', 'Статистика'])

print('Всі студенти:')
for sid, data in students.items():
    print(' ', sid, data)

print('Пошук Анна:', find_by_name(students, 'Анна'))
print('Пошук Петро:', find_by_name(students, 'Петро'))
print('Топ-3:', top_students(students))
print('На курсі Python:', students_in_course(students, 'Python'))
print('Спільні курси ST-001 і ST-004:', common_courses(students, 'ST-001', 'ST-004'))
print('Статистика:', stats(students))

by_courses = {}
for data in students.values():
    by_courses.setdefault(data[3], []).append(data[0])

print('Студенти з однаковим набором курсів:')
for course_set, names in by_courses.items():
    if len(names) > 1:
        print(' ', sorted(course_set), '->', names)