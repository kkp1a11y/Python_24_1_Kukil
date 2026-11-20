import os

SRC = os.path.join('lab6_data', 'students.txt')
DST = os.path.join('lab6_data', 'students_upper.txt')


def main():
    try:
        lines = []
        with open(SRC, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, start=1):
                print(f'{i:3}: {line}', end='')
                lines.append(line)
        print()

        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        size = os.path.getsize(SRC)

        print(f'Кількість рядків: {line_count}')
        print(f'Кількість слів:   {word_count}')
        print(f'Розмір файлу:     {size} байт')

        with open(DST, 'w', encoding='utf-8') as out:
            for line in lines:
                out.write(line.upper())
        print(f'Результат записано у {DST}')

    except FileNotFoundError:
        print(f'Файл не знайдено: {SRC}')
    except UnicodeDecodeError:
        print('Помилка кодування: збережіть файл у UTF-8 '
              'або вкажіть encoding="cp1251"')


if __name__ == '__main__':
    main()