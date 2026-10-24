import logging

logging.basicConfig(
    filename='errors.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8',
)


def demonstrate_exceptions():
    logging.info('Початок демонстрації винятків')

    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        logging.error('ZeroDivisionError: %s', e)

    try:
        number = int('abc')
    except ValueError as e:
        logging.error('ValueError: %s', e)

    try:
        lst = [1, 2, 3]
        print(lst[10])
    except IndexError as e:
        logging.error('IndexError: %s', e)

    try:
        data = {'name': 'Anna'}
        print(data['age'])
    except KeyError as e:
        logging.error('KeyError: ключ %s відсутній у словнику', e)

    try:
        open('nofile.txt', encoding='utf-8')
    except FileNotFoundError as e:
        logging.error('FileNotFoundError: %s', e)

    try:
        result = 5 % 0
    except ArithmeticError as e:
        logging.warning(
            'ArithmeticError перехопив %s: %s', type(e).__name__, e
        )

    errors = [
        lambda: 1 / 0,
        lambda: int('x'),
        lambda: [][0],
        lambda: {}['k'],
        lambda: open('nofile.txt'),
    ]
    for action in errors:
        try:
            action()
        except Exception as e:
            logging.warning(
                'Exception перехопив %s: %s', type(e).__name__, e
            )

    logging.debug(
        'issubclass(KeyboardInterrupt, Exception) = %s',
        issubclass(KeyboardInterrupt, Exception),
    )
    logging.debug(
        'issubclass(KeyboardInterrupt, BaseException) = %s',
        issubclass(KeyboardInterrupt, BaseException),
    )

    try:
        try:
            raise KeyboardInterrupt
        except Exception:
            logging.error('Цей рядок не з\'явиться: Exception не ловить KeyboardInterrupt')
    except KeyboardInterrupt:
        logging.warning('KeyboardInterrupt пройшов повз except Exception, його піймав лише зовнішній блок')

    logging.info('Демонстрацію завершено')


demonstrate_exceptions()

logging.shutdown()
print('--- Вміст errors.log ---')
with open('errors.log', 'r', encoding='utf-8') as f:
    print(f.read())