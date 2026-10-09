odd_squares = [x**2 for x in range(1, 21) if x % 2 != 0]
print('Квадрати непарних:', odd_squares)

sentence = input('Введіть речення: ')
lengths = [len(w) for w in sentence.split() if len(w) > 3]
print('Довжини слів (>3):', lengths)

table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
for row in table:
    print(row)

flat = [x for row in table for x in row]
print('Сплощена:', flat)

pairs = [(i, j) for i in range(1, 6) for j in range(1, 6) if i < j]
print('Пари:', pairs)