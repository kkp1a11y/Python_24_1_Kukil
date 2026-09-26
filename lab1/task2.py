import math

a = float(input('Введіть перше число: '))
b = float(input('Введіть друге число: '))

print(f'{a} + {b} = {a + b:.2f}')
print(f'{a} - {b} = {a - b:.2f}')
print(f'{a} * {b} = {a * b:.2f}')

if b != 0:
    print(f'{a} / {b} = {a / b:.2f}')
    print(f'{a} // {b} = {a // b:.2f}')
    print(f'{a} % {b} = {a % b:.2f}')
else:
    print('Ділення на нуль неможливе')

print(f'{a} ** {b} = {a ** b:.2f}')

hypotenuse = math.sqrt(a ** 2 + b ** 2)
print(f'Гіпотенуза при катетах {a} і {b}: {hypotenuse:.2f}')