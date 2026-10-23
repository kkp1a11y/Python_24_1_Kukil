numbers = range(-10, 11)
multiples_of_3 = list(filter(lambda x: x % 3 == 0, numbers))
print('--- кратні 3 ---')
print(multiples_of_3)


celsius = [0, 20, 37, 100]
kelvin = list(map(lambda c: c + 273.15, celsius))
print('--- Кельвіни ---')
print(kelvin)


words = ['яблуко', 'банан', 'кіт', 'вишня', 'слива', 'дім']
by_last_letter = sorted(words, key=lambda w: w[-1])
print('--- за останньою літерою ---')
print(by_last_letter)


people = [
    {'name': 'Іван', 'age': 22},
    {'name': 'Марія', 'age': 19},
    {'name': 'Олег', 'age': 21},
    {'name': 'Анна', 'age': 25},
    {'name': 'Денис', 'age': 20},
]
adults = sorted(
    filter(lambda p: p['age'] >= 21, people),
    key=lambda p: p['name']
)
print('--- вік >= 21, за іменем ---')
print(adults)
