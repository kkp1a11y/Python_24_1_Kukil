students = [
    ('Шевченко', 4.7), ('Коваленко', 3.8), ('Бондаренко', 4.2),
    ('Ткаченко', 3.5), ('Мельник', 4.9), ('Кравчук', 3.9),
    ('Олійник', 4.0), ('Лисенко', 3.2),
]

print('За балом (спад.):')
for name, gpa in sorted(students, key=lambda s: s[1], reverse=True):
    print(f'  {name}: {gpa}')

print('За прізвищем:')
for name, gpa in sorted(students, key=lambda s: s[0]):
    print(f'  {name}: {gpa}')

best = max(students, key=lambda s: s[1])
worst = min(students, key=lambda s: s[1])
print('Максимальний бал:', best)
print('Мінімальний бал:', worst)

good = [s for s in students if s[1] >= 4.0]
print('Бал >= 4.0:', good)

gpas = [s[1] for s in students]
print(f'Середній бал групи: {sum(gpas) / len(gpas):.2f}')

surnames = [s[0] for s in students]
print('Прізвища:', ', '.join(surnames))