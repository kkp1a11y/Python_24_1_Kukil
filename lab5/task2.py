def read_numbers_from_file(filename):
    numbers = []
    line_no = 0
    text = ''

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line_no, line in enumerate(f, start=1):
                text = line.strip()
                if not text:
                    continue
                numbers.append(float(text))
    except FileNotFoundError:
        print(f'Файл "{filename}" не знайдено')
        return []
    except ValueError as e:
        print(f'Не вдалося перетворити рядок {line_no} ("{text}") у число: {e}')
        return []
    else:
        print(f'Файл прочитано успішно: {len(numbers)} чисел')
    finally:
        print('Файл закрито')

    return numbers


print('--- Тест 1: існуючий файл із помилковим рядком ---')
print(read_numbers_from_file('numbers.txt'))

print('\n--- Тест 2: неіснуючий файл ---')
print(read_numbers_from_file('no_such_file.txt'))