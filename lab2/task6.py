text = """Python - це проста та потужна мова програмування. Вона дозволяє швидко писати код! Багато студентів починають вивчення програмування саме з Python. Чи важко вчити нову мову? Ні, якщо практикуватися щодня, мова стає зрозумілою. Level, radar та шалаш - це приклади паліндромів."""

print('Символів (з пробілами):', len(text))
print('Символів (без пробілів):', len(text.replace(' ', '').replace('\n', '')))

raw_words = text.split()
words = [w.strip('.,!?;:').lower() for w in raw_words]
words = [w for w in words if w.isalpha()]

print('Слів:', len(words))

sentences = [s for s in
             text.replace('!', '.').replace('?', '.').split('.')
             if s.strip()]
print('Речень:', len(sentences))
print('Унікальних слів:', len(set(words)))

unique_words = sorted(set(words))
freq = [(w, words.count(w)) for w in unique_words]

top5 = sorted(freq, key=lambda p: p[1], reverse=True)[:5]
print('Топ-5 слів:')
for w, c in top5:
    print(f'  {w}: {c}')

print('Найдовше слово:', max(words, key=len))
print('Найчастіше слово:', top5[0][0])

pal = [w for w in set(words) if len(w) > 1 and w == w[::-1]]
print('Паліндромів:', len(pal), pal)

summary = text[:80] + '...' if len(text) > 80 else text
print('Резюме:', summary)

print('\nВведіть оцінки у форматі "Прізвище:оцінка" (порожній рядок - кінець):')
records = []
while True:
    line = input()
    if not line.strip():
        break
    name, grade = line.split(':')
    records.append((name.strip(), float(grade)))

if records:
    rating = sorted(records, key=lambda r: r[1], reverse=True)
    print('Рейтинг:')
    for i, (name, grade) in enumerate(rating, start=1):
        print(f'  {i}. {name}: {grade}')

    avg = sum(g for _, g in records) / len(records)
    above = [n for n, g in records if g > avg]
    below = [n for n, g in records if g < avg]

    print(f'Середня оцінка: {avg:.2f}')
    print('Вище середньої:', len(above))
    print('Нижче середньої:', len(below))

    report = ' | '.join([
        f'Студентів: {len(records)}',
        f'Середня: {avg:.2f}',
        f'Найкращий: {rating[0][0]} ({rating[0][1]})',
        f'Вище середньої: {len(above)}',
        f'Нижче середньої: {len(below)}',
    ])
    print('\nЗВІТ:', report)