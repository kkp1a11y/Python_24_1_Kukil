import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / 'lab6_data'
SOURCE_FILE = DATA_DIR / 'contacts.txt'
RESULT_FILE = DATA_DIR / 'results.txt'

EMAIL_PATTERN = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

PHONE_PATTERN = (
    r'(?<!\w)'
    r'(?:\+38[ \t-]?)?'
    r'(?:\(0\d{2}\)|0[ \t-]?\d{2})'
    r'[ \t-]?\d{3}'
    r'[ \t-]?\d{2}'
    r'[ \t-]?\d{2}'
    r'(?!\w)'
)

DATE_PATTERN = r'\b(\d{2})\.(\d{2})\.(\d{4})\b'


def main():
    try:
        with open(SOURCE_FILE, 'r', encoding='utf-8') as file:
            text = file.read()

        emails = re.findall(EMAIL_PATTERN, text)
        phones = re.findall(PHONE_PATTERN, text)

        dates = [
            re.sub(DATE_PATTERN, r'\3-\2-\1', match.group())
            for match in re.finditer(DATE_PATTERN, text)
        ]

        sections = [
            ('EMAIL-АДРЕСИ', emails),
            ('НОМЕРИ ТЕЛЕФОНІВ', phones),
            ('ДАТИ У ФОРМАТІ ISO', dates),
        ]

        with open(RESULT_FILE, 'w', encoding='utf-8') as file:
            for title, items in sections:
                print(f'\n--- {title} ---')
                file.write(f'--- {title} ---\n')

                for item in items:
                    print(item)
                    file.write(item + '\n')

                file.write('\n')

        print('\n--- Підсумок ---')
        print(f'Email-адрес: {len(emails)}')
        print(f'Телефонів: {len(phones)}')
        print(f'Дат: {len(dates)}')
        print(f'Результат записано у: {RESULT_FILE}')

    except FileNotFoundError:
        print(f'Помилка: файл не знайдено: {SOURCE_FILE}')
    except PermissionError:
        print('Помилка: немає прав для читання або запису.')
    except UnicodeDecodeError:
        print('Помилка: збережіть contacts.txt у кодуванні UTF-8.')
    except OSError as error:
        print(f'Помилка файлової системи: {error}')


if __name__ == '__main__':
    main()