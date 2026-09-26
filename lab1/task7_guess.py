secret_number = 67
max_attempts = 7
attempts = 0

while attempts < max_attempts:
    guess = int(input('Вгадайте число від 1 до 100: '))
    attempts += 1

    if guess == secret_number:
        print(f'Вітаю! Ви вгадали число за {attempts} спроб(и)')
        break
    elif guess < secret_number:
        print('Більше')
    else:
        print('Менше')
else:
    print(f'Спроби вичерпано. Загадане число було: {secret_number}')