month = int(input('Введіть номер місяця (1-12): '))

match month:
    case 12 | 1 | 2:
        season = 'Зима'
    case 3 | 4 | 5:
        season = 'Весна'
    case 6 | 7 | 8:
        season = 'Літо'
    case 9 | 10 | 11:
        season = 'Осінь'
    case _:
        season = None

if season is None:
    print('Некоректний номер місяця')
else:
    match month:
        case 4 | 6 | 9 | 11:
            days = 30
        case 2:
            days = 28
        case _:
            days = 31
    print(f'Пора року: {season}')
    print(f'Кількість днів у місяці: {days}')