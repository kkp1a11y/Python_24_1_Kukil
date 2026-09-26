n = int(input('Скільки чисел ви введете: '))

numbers = []
total = 0
minimum = None
maximum = None
divisible_by_3 = 0
divisible_by_5 = 0
divisible_by_both = 0

for i in range(n):
    value = float(input(f'Введіть число {i + 1}: '))
    numbers.append(value)
    total += value

    if minimum is None or value < minimum:
        minimum = value
    if maximum is None or value > maximum:
        maximum = value

    if value % 3 == 0:
        divisible_by_3 += 1
    if value % 5 == 0:
        divisible_by_5 += 1
    if value % 3 == 0 and value % 5 == 0:
        divisible_by_both += 1

average = total / n if n > 0 else 0

print(f'Сума: {total:.2f}')
print(f'Середнє арифметичне: {average:.2f}')
print(f'Мінімум: {minimum}')
print(f'Максимум: {maximum}')
print(f'Кратних 3: {divisible_by_3}')
print(f'Кратних 5: {divisible_by_5}')
print(f'Кратних одночасно 3 і 5: {divisible_by_both}')

print('Числа у зворотньому порядку:')
for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i], end=' ')
print()