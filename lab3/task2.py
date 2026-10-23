grades = {'Математика': 90, 'Фізика': 85, 'Python': 95,
          'Англійська': 80, 'Історія': 75, 'Бази даних': 88}

print('Предмети:', list(grades.keys()))
print('Оцінки:', list(grades.values()))

for subject, mark in grades.items():
    print(f'{subject}: {mark}')

best = max(grades, key=grades.get)
print('Найвища оцінка:', best, grades[best])

avg = sum(grades.values()) / len(grades)
print(f'Середня: {avg:.2f}')

grades['Хімія'] = 78
grades['Історія'] = 82
removed = grades.pop('Фізика')
print('Видалено оцінку:', removed)

sorted_grades = dict(sorted(grades.items(), key=lambda x: x[1], reverse=True))
print(sorted_grades)