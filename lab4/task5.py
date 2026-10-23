import time
from functools import reduce, wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f'\n{func.__name__} виконано за {elapsed:.4f} с')
        return result
    return wrapper


students = [
    {'name': 'Іван',   'year': 1, 'grades': [85, 90, 78, 92, 88]},
    {'name': 'Марія',  'year': 2, 'grades': [95, 98, 92, 96, 94]},
    {'name': 'Олег',   'year': 1, 'grades': [60, 55, 70, 65, 58]},
    {'name': 'Анна',   'year': 3, 'grades': [88, 91, 85, 90, 87]},
    {'name': 'Денис',  'year': 2, 'grades': [72, 68, 75, 70, 66]},
    {'name': 'Софія',  'year': 3, 'grades': [97, 93, 99, 95, 96]},
    {'name': 'Андрій', 'year': 4, 'grades': [45, 52, 38, 60, 49]},
    {'name': 'Ліна',   'year': 4, 'grades': [80, 77, 85, 79, 83]},
    {'name': 'Тарас',  'year': 2, 'grades': [91, 89, 94, 90, 92]},
]


def average(grades):
    if not grades:
        return 0
    total = reduce(lambda acc, g: acc + g, grades, 0)
    return round(total / len(grades), 2)


def classify(avg):
    if avg >= 90:
        return 'відмінник'
    if avg >= 75:
        return 'хорошист'
    if avg >= 60:
        return 'задовільно'
    return 'незараховано'


def make_year_filter(year):
    return lambda s: s['year'] == year

def make_category_filter(category):
    return lambda s: classify(average(s['grades'])) == category


def get_top(students, n=3):
    return sorted(students,
                  key=lambda s: average(s['grades']),
                  reverse=True)[:n]


def group_by_year(students):
    years = sorted(set(map(lambda s: s['year'], students)))
    return {y: list(filter(make_year_filter(y), students)) for y in years}


@timer
def report(students):
    avgs = list(map(lambda s: average(s['grades']), students))

    print('=== Загальне зведення ===')
    print(f'Кількість студентів: {len(students)}')
    print(f'Середній бал по групі: {average(avgs)}')
    best = get_top(students, 1)[0]
    worst = sorted(students, key=lambda s: average(s['grades']))[0]
    print(f'Найкращий: {best["name"]} ({average(best["grades"])})')
    print(f'Найнижчий: {worst["name"]} ({average(worst["grades"])})')

    print('\n=== Топ-3 ===')
    for place, s in enumerate(get_top(students, 3), start=1):
        print(f'{place}. {s["name"]} — {average(s["grades"])}')

    print('\n=== Розбивка по курсах ===')
    for year, group in group_by_year(students).items():
        names = ', '.join(map(lambda s: s['name'], group))
        year_avg = average(list(map(lambda s: average(s['grades']), group)))
        print(f'{year} курс: {names} (середній бал {year_avg})')

    print('\n=== Розподіл за категоріями ===')
    categories = ['відмінник', 'хорошист', 'задовільно', 'незараховано']
    for cat in categories:
        found = list(filter(make_category_filter(cat), students))
        names = ', '.join(map(lambda s: s['name'], found)) or '—'
        print(f'{cat}: {len(found)} ({names})')


report(students)