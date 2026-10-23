def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print('--- power ---')
print(power(2, 5))
print(power(3, 4))
print(power(10, 0))
print(power(7, 1))


def factorial(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)

print('--- factorial ---')
print(factorial(5))
print(factorial(0))
print(factorial(7))
print(factorial(10))