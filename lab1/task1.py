num_int1, num_int2 = 25, -10
num_float1, num_float2 = 3.14, -0.5
str1, str2 = 'Python', 'Лабораторна'
bool1, bool2 = True, False

print(num_int1, type(num_int1))
print(num_int2, type(num_int2))
print(num_float1, type(num_float1))
print(num_float2, type(num_float2))
print(str1, type(str1))
print(str2, type(str2))
print(bool1, type(bool1))
print(bool2, type(bool2))

str_number = '123'
converted_to_int = int(str_number)
converted_to_str = str(num_int1)
print('Рядок у число:', converted_to_int, type(converted_to_int))
print('Число у рядок:', converted_to_str, type(converted_to_str))

print('a', 'b', 'c', sep=' | ')
print('Значення:', num_int1, num_float1, sep=' -> ')
print('Перший рядок', end=' *** ')
print('Другий рядок')