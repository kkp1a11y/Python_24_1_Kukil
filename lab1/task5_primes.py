n = int(input('Введіть N: '))

print(f'Прості числа від 2 до {n}:')
for number in range(2, n + 1):
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            break
    else:
        print(number, end=' ')
print()