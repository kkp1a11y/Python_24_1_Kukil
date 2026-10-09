sentence = input('Введіть речення: ')
words = sentence.split()

print('Слова:', words)
print('Кількість слів:', len(words))
print('Найдовше:', max(words, key=len))
print('Найкоротше:', min(words, key=len))

print('За алфавітом:', ', '.join(sorted(words, key=str.lower)))
print('Реверс:', words[::-1])

palindromes = [w for w in words if w.lower() == w.lower()[::-1]]
print('Паліндроми:', palindromes)