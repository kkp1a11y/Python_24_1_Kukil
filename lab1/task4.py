total = 0
count = 0
minimum = None
maximum = None
negative_count = 0
positive_count = 0

while True:
    value = float(input('Введіть число (0 для завершення): '))
    if value == 0:
        break

    total += value
    count += 1

    if minimum is None or value < minimum:
        minimum = value
    if maximum is None or value > maximum:
        maximum = value

    if value > 0:
        positive_count += 1
    else:
        negative_count += 1

    if count == 0:
        print('Жодного числа не було введено')
    else:
        average = total / count
        print(f'Сума: {total:.2f}')
        print(f'Кількість чисел: {count}')
        print(f'Середнє арифметичне: {average:.2f}')
        print(f'Мінімум: {minimum:.2f}')
        print(f'Максимум: {maximum:.2f}')
        print(f'Кількість від\'ємних чисел: {negative_count}')
        print(f'Кількість додатних чисел: {positive_count}')