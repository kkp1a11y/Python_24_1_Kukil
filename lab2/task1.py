s = input('Введіть рядок: ')

print('Довжина:', len(s))
if s:
    print('Перший символ:', s[0])
    print('Останній символ:', s[-1])

print('Верхній регістр:', s.upper())
print('Нижній регістр:', s.lower())
print('Title:', s.title())
print('Реверс:', s[::-1])

ch = input('Введіть літеру для підрахунку (Enter = "а"): ') or 'а'
print(f'Кількість "{ch}":', s.lower().count(ch.lower()))

sub = input('Введіть підрядок для перевірки: ')
print('Починається з підрядка:', s.startswith(sub))
print('Закінчується підрядком:', s.endswith(sub))

print('Заміна пробілів:', s.replace(' ', '_'))