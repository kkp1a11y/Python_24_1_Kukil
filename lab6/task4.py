import shutil
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / 'lab6_data'
BACKUP_DIR = BASE_DIR / 'backup'


def backup_file(src_path):
    src_path = Path(src_path)

    try:
        if not src_path.is_file():
            raise FileNotFoundError(f'Файл не знайдено: {src_path}')

        BACKUP_DIR.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
        backup_name = (
            f'{src_path.stem}_{timestamp}{src_path.suffix}'
        )
        destination = BACKUP_DIR / backup_name

        shutil.copy2(src_path, destination)

        print(f'Створено резервну копію: {destination.name}')
        return destination

    except FileNotFoundError as error:
        print(f'Помилка: {error}')
    except PermissionError:
        print('Помилка: немає прав для копіювання файлу.')
    except OSError as error:
        print(f'Помилка копіювання: {error}')

    return None


def backup_folder(src_dir, dst_dir):
    try:
        shutil.copytree(
            src_dir,
            dst_dir,
            ignore=shutil.ignore_patterns('*.tmp', '*.log')
        )

        print(f'Директорію скопійовано до: {dst_dir}')
        return Path(dst_dir)

    except FileNotFoundError:
        print(f'Помилка: вихідну директорію не знайдено: {src_dir}')
    except PermissionError:
        print('Помилка: немає прав для копіювання директорії.')
    except FileExistsError:
        print(f'Помилка: директорія призначення вже існує: {dst_dir}')
    except shutil.Error as error:
        print(f'Помилки копіювання окремих файлів: {error}')
    except OSError as error:
        print(f'Помилка файлової системи: {error}')

    return None


def restore_latest(filename):
    destination = Path(filename)

    try:
        pattern = f'{destination.stem}_*{destination.suffix}'
        copies = sorted(
            path for path in BACKUP_DIR.glob(pattern)
            if path.is_file()
        )

        if not copies:
            raise FileNotFoundError(
                f'Немає резервних копій для {destination.name}'
            )

        latest = copies[-1]

        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(latest, destination)

        print(f'Файл відновлено з копії: {latest.name}')
        return destination

    except FileNotFoundError as error:
        print(f'Помилка: {error}')
    except PermissionError:
        print('Помилка: немає прав для відновлення файлу.')
    except OSError as error:
        print(f'Помилка відновлення: {error}')

    return None


def main():
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)

        demo_file = DATA_DIR / 'backup_demo.txt'

        with open(demo_file, 'w', encoding='utf-8') as file:
            file.write('Початковий текст для резервного копіювання.\n')

        print('--- Резервне копіювання файлу ---')
        copy_path = backup_file(demo_file)

        if copy_path is None:
            return

        with open(demo_file, 'w', encoding='utf-8') as file:
            file.write('Змінений текст після створення копії.\n')

        print('\n--- Вміст після зміни ---')
        with open(demo_file, 'r', encoding='utf-8') as file:
            print(file.read(), end='')

        print('\n--- Відновлення файлу ---')
        restored = restore_latest(demo_file)

        if restored is not None:
            with open(restored, 'r', encoding='utf-8') as file:
                print(file.read(), end='')

        for name in ('backup_demo.tmp', 'backup_demo.log'):
            with open(DATA_DIR / name, 'w', encoding='utf-8') as file:
                file.write('Цей файл не повинен потрапити до копії.\n')

        print('\n--- Резервне копіювання директорії ---')
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
        folder_copy = BACKUP_DIR / f'lab6_data_{timestamp}'

        result = backup_folder(DATA_DIR, folder_copy)

        if result is not None:
            print('\nФайли у резервній директорії:')
            for path in sorted(result.rglob('*')):
                if path.is_file():
                    print(path.relative_to(result))

            excluded = [
                path for path in result.rglob('*')
                if path.is_file() and path.suffix in ('.tmp', '.log')
            ]
            print(f'\nФайлів .tmp і .log у копії: {len(excluded)}')

    except FileNotFoundError as error:
        print(f'Файл або директорію не знайдено: {error}')
    except PermissionError:
        print('Помилка: немає прав доступу.')
    except UnicodeDecodeError:
        print('Помилка: файл повинен мати кодування UTF-8.')
    except OSError as error:
        print(f'Помилка файлової системи: {error}')


if __name__ == '__main__':
    main()