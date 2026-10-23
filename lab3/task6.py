schedule = {
    'Понеділок': [('08:30', 'Python', '301'), ('10:10', 'Математика', '215'), ('11:50', 'Фізика', '112')],
    'Вівторок':  [('08:30', 'Бази даних', '301'), ('10:10', 'Англійська', '118')],
    'Середа':    [('10:10', 'Python', '305'), ('11:50', 'Історія', '215'),
                  ('13:30', 'Математика', '215'), ('15:10', 'Фізика', '112')],
    'Четвер':    [('08:30', 'Англійська', '118')],
    'П\'ятниця': [('10:10', 'Бази даних', '301'), ('11:50', 'Python', '305')],
}

rooms = {room for lessons in schedule.values() for _, _, room in lessons}
print('Унікальні аудиторії:', sorted(rooms))

print('Понеділок:')
for time, subject, room in schedule['Понеділок']:
    print(f'  {time} — {subject} (ауд. {room})')

busiest = max(schedule, key=lambda day: len(schedule[day]))
print('Найбільше занять:', busiest, len(schedule[busiest]))

transactions = [
    ('2026-10-01', 'Їжа', 250), ('2026-10-01', 'Транспорт', 40),
    ('2026-10-02', 'Розваги', 300), ('2026-10-02', 'Їжа', 180),
    ('2026-10-03', 'Навчання', 1200), ('2026-10-04', 'Їжа', 320),
    ('2026-10-04', 'Транспорт', 60), ('2026-10-05', 'Розваги', 150),
    ('2026-10-06', 'Їжа', 210), ('2026-10-07', 'Транспорт', 45),
    ('2026-10-07', 'Навчання', 500), ('2026-10-08', 'Їжа', 275),
    ('2026-10-09', 'Розваги', 420), ('2026-10-10', 'Транспорт', 50),
    ('2026-10-10', 'Їжа', 190),
]

totals = {}
for date, category, amount in transactions:
    totals[category] = totals.get(category, 0) + amount
print('Витрати по категоріях:', totals)

unique_dates = {date for date, _, _ in transactions}
print('Унікальних дат:', len(unique_dates), sorted(unique_dates))

top_cat = max(totals, key=totals.get)
print('Найбільші витрати:', top_cat, totals[top_cat])