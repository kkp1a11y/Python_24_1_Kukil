from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / 'lab6_data' / 'events.log'


def log_event(filename, level, message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f'[{timestamp}] [{level}] {message}\n')


def read_log(filename, level=None):
    records = []

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            record = line.rstrip('\n')

            if level is None:
                records.append(record)
            else:
                parts = record.split('] ', maxsplit=2)

                if len(parts) == 3 and parts[1] == f'[{level}':
                    records.append(record)

    return records


def main():
    try:
        LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

        events = [
            ('INFO', 'Запуск програми'),
            ('INFO', 'Відкриття файлу студентів'),
            ('WARNING', 'Знайдено порожній рядок'),
            ('INFO', 'Дані студентів прочитано'),
            ('ERROR', 'Не знайдено файл налаштувань'),
            ('INFO', 'Застосовано стандартні налаштування'),
            ('WARNING', 'Виявлено повторний запис'),
            ('ERROR', 'Некоректний формат оцінки'),
            ('INFO', 'Результати збережено'),
            ('INFO', 'Завершення програми'),
        ]

        for level, message in events:
            log_event(LOG_FILE, level, message)

        print('--- Усі записи журналу ---')
        for record in read_log(LOG_FILE):
            print(record)

        print('\n--- Записи рівня ERROR ---')
        for record in read_log(LOG_FILE, 'ERROR'):
            print(record)

        print('\n--- Кількість записів кожного рівня ---')
        for level in ('INFO', 'WARNING', 'ERROR'):
            print(f'{level}: {len(read_log(LOG_FILE, level))}')

        print(f'\nЖурнал: {LOG_FILE}')

    except FileNotFoundError:
        print('Помилка: файл журналу не знайдено.')
    except PermissionError:
        print('Помилка: немає прав доступу до журналу.')
    except UnicodeDecodeError:
        print('Помилка: файл журналу повинен мати кодування UTF-8.')
    except OSError as error:
        print(f'Помилка файлової системи: {error}')


if __name__ == '__main__':
    main()