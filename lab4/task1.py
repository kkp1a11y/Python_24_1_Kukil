def is_even(n):
    return n % 2 == 0

print('--- is_even ---')
print(is_even(4))
print(is_even(7))
print(is_even(0))
print(is_even(-6))


def max_of_three(a, b, c):
    result = a
    if b > result:
        result = b
    if c > result:
        result = c
    return result

print('--- max_of_three ---')
print(max_of_three(3, 9, 5))
print(max_of_three(10, 2, 7))
print(max_of_three(-1, -5, -3))
print(max_of_three(4, 4, 4))



def power(base, exp=2):
    return base ** exp

print('--- power ---')
print(power(5))
print(power(2, 10))
print(power(3, exp=3))
print(power(10, 0))