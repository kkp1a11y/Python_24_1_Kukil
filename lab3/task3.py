students_math = {'Іваненко', 'Петренко', 'Сидоренко', 'Коваль', 'Мельник', 'Бондар'}
students_physics = {'Петренко', 'Коваль', 'Шевченко', 'Мельник', 'Ткачук'}
students_cs = {'Коваль', 'Мельник', 'Шевченко', 'Лисенко', 'Бондар'}

print('Усі три предмети:', students_math & students_physics & students_cs)
print('Хоча б один:', students_math | students_physics | students_cs)
print('Математика без фізики:', students_math - students_physics)
print('cs ⊆ math?', students_cs.issubset(students_math))

# Рівно два предмети
all_students = students_math | students_physics | students_cs
exactly_two = {
    s for s in all_students
    if (s in students_math) + (s in students_physics) + (s in students_cs) == 2
}
print('Рівно два:', exactly_two)

# Дублікати
print(list(set([1, 2, 2, 3, 3, 3, 4])))