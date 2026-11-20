from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / 'lab6_data'
PROJECT_DIR = BASE_DIR / 'lab6_project'


def print_tree(directory, depth=0):
    print('    ' * depth + directory.name + '/')

    for item in sorted(directory.iterdir()):
        if item.is_dir() and not item.is_symlink():
            print_tree(item, depth + 1)
        else:
            print('    ' * (depth + 1) + item.name)


def main():
    try:
        for name in ('src', 'data', 'output'):
            (PROJECT_DIR / name).mkdir(
                parents=True,
                exist_ok=True
            )

        print('--- Структура директорій ---')
        print_tree(PROJECT_DIR)

        print('\n--- Інформація про файли lab6_data ---')

        for path in sorted(DATA_DIR.iterdir()):
            if path.is_file():
                info = path.stat()
                modified = datetime.fromtimestamp(info.st_mtime)

                print(f'\nНазва: {path.name}')
                print(f'Розширення: {path.suffix or "відсутнє"}')
                print(f'Розмір: {info.st_size} байт')
                print(
                    'Остання зміна:',
                    modified.strftime('%d.%m.%Y %H:%M:%S')
                )

        print('\n--- Текстові файли через glob ---')

        for path in sorted(DATA_DIR.glob('*.txt')):
            if path.is_file():
                print(path.name)

    except FileNotFoundError:
        print('Помилка: папку lab6_data не знайдено.')
    except PermissionError:
        print('Помилка: немає прав доступу до файлів або папок.')
    except OSError as error:
        print(f'Помилка файлової системи: {error}')


if __name__ == '__main__':
    main()