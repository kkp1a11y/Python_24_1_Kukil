cubes = {n: n**3 for n in range(1, 11)}
print(cubes)

prices = {'яблуко': 35, 'банан': 22, 'ківі': 55, 'слива': 18}
cheap = {k: v for k, v in prices.items() if v < 40}
print(cheap)

students = [
    {'name': 'Іван', 'gpa': 4.2},
    {'name': 'Марія', 'gpa': 4.8},
    {'name': 'Олег', 'gpa': 3.6},
    {'name': 'Анна', 'gpa': 4.5},
    {'name': 'Денис', 'gpa': 3.9},
]
gpa_dict = {s['name']: s['gpa'] for s in students}
print(gpa_dict)

phonebook = {
    'Іван':  {'phone': '+380501112233', 'email': 'ivan@mail.com',  'city': 'Київ'},
    'Марія': {'phone': '+380672223344', 'email': 'maria@mail.com', 'city': 'Львів'},
    'Олег':  {'phone': '+380933334455', 'email': 'oleg@mail.com',  'city': 'Київ'},
}

print('Контакти з Києва:')
for name, info in phonebook.items():
    if info['city'] == 'Київ':
        print(f"  {name}: {info['phone']}")

phonebook['Анна'] = {'phone': '+380634445566', 'email': 'anna@mail.com', 'city': 'Одеса'}

print(phonebook.get('Петро', {}).get('email', 'контакт не знайдено'))