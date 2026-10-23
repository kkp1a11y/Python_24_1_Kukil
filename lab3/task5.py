text = ('Python is a great language and Python is easy to learn because Python '
        'has simple syntax and the community is great and friendly so many '
        'people learn Python every year and build great projects with Python')
words = text.lower().split()
print('Усього слів:', len(words))

word_count = {}
for w in words:
    if w in word_count:
        word_count[w] += 1
    else:
        word_count[w] = 1
print(word_count)

top3 = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:3]
print('Топ-3:', top3)

char_count = {}
for ch in text.lower():
    if ch.isalpha():
        char_count[ch] = char_count.get(ch, 0) + 1
print(char_count)

reverse_index = {}
for i, w in enumerate(words):
    reverse_index.setdefault(w, []).append(i)
print(reverse_index)

# 5. Унікальні слова
unique_count = len(word_count)
print(f'Унікальних слів: {unique_count}')
print(f'Відсоток унікальних: {unique_count / len(words) * 100:.1f}%')