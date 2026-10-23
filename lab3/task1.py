cities = ('Київ', 'Львів', 'Одеса', 'Харків', 'Дніпро')
print('Перше:', cities[0])
print('Останнє:', cities[-1])
print('Зворотно:', cities[::-1])
print('Довжина:', len(cities))

def minmax(numbers):
    return min(numbers), max(numbers)
lo, hi = minmax([4, 9, -3, 12, 7])
print('Мін:', lo, 'Макс:', hi)

first, *middle, last = (1, 2, 3, 4, 5)
print(first, middle, last)

a, b, c = 1, 2, 3
a, b, c = b, c, a
print(a, b, c)

not_tuple = (5)
is_tuple = (5,)
print(type(not_tuple))
print(type(is_tuple))