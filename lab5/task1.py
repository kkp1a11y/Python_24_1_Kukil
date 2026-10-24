def safe_calculator():
    success_count = 0
    error_count = 0
    operations = ('+', '-', '*', '/', '//', '%')

    print("Калькулятор. Для виходу введіть 'q' на місці першого числа.")

    while True:
        first = input("\nПерше число (або 'q' для виходу): ").strip()
        if first.lower() == 'q':
            break

        try:
            a = float(first)
            b = float(input("Друге число: ").strip())

            op = input(f"Операція ({', '.join(operations)}): ").strip()
            if op not in operations:
                raise ValueError(f'Невідома операція "{op}". Дозволені: {", ".join(operations)}')

            if op == '+':
                result = a + b
            elif op == '-':
                result = a - b
            elif op == '*':
                result = a * b
            elif op == '/':
                result = a / b
            elif op == '//':
                result = a // b
            else:
                result = a % b

        except ZeroDivisionError:
            print('Помилка: ділення на нуль неможливе!')
            error_count += 1
        except ValueError as e:
            if 'could not convert' in str(e):
                print('Помилка: введено не число!')
            else:
                print(f'Помилка: {e}')
            error_count += 1
        else:
            print(f'Результат: {a} {op} {b} = {result}')
            success_count += 1

    print('\n--- Підсумок ---')
    print(f'Успішних обчислень: {success_count}')
    print(f'Помилок: {error_count}')


if __name__ == '__main__':
    safe_calculator()