nums = []
for i in range(8):
    nums.append(int(input(f'Число {i + 1}: ')))

print('Список:', nums)
print('Довжина:', len(nums))
print('Сума:', sum(nums))
print('Мінімум:', min(nums))
print('Максимум:', max(nums))

print('Перший:', nums[0], '| Останній:', nums[-1])
print('Перші три:', nums[:3])
print('Останні три:', nums[-3:])

print('Відсортований:', sorted(nums))
print('Оригінал:', nums)

print('Без дублікатів:', list(set(nums)))

avg = sum(nums) / len(nums)
print(f'Середнє: {avg:.2f}')
print('Більші за середнє:', [x for x in nums if x > avg])