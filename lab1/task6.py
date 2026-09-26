calculations_count = 0

while True:
    a = float(input('Введіть перше число: '))
    b = float(input('Введіть друге число: '))
    operation = input('Введіть операцію (+, -, *, /, //, %, **): ')

    match operation:
        case '+':
            result = a + b
        case '-':
            result = a - b
        case '*':
            result = a * b
        case '/':
            if b == 0:
                print('Помилка: ділення на нуль')
                result = None
            else:
                result = a / b
        case '//':
            if b == 0:
                print('Помилка: ділення на нуль')
                result = None
            else:
                result = a // b
        case '%':
            if b == 0:
                print('Помилка: ділення на нуль')
                result = None
            else:
                result = a % b
        case '**':
            result = a ** b
        case _:
            print('Невідома операція')
            result = None

    if result is not None:
        print(f'Результат: {result:.2f}')
        calculations_count += 1

    answer = input('Продовжити? (y/n): ')
    if answer.lower() == 'n':
        break

print(f'Кількість виконаних обчислень: {calculations_count}')