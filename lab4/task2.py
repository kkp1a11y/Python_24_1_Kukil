def sum_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print('--- sum_list ---')
print(sum_list([1, 2, 3]))
print(sum_list([10, 20, 30, 40, 50]))
print(sum_list([7]))
print(sum_list([]))


def stats(*numbers):
    if not numbers:
        return None
    total = sum(numbers)
    return {
        'min': min(numbers),
        'max': max(numbers),
        'sum': total,
        'avg': round(total / len(numbers), 2),
    }

print('--- stats ---')
print(stats(5))
print(stats(4, 8, 15))
print(stats(3, 9, 1, 7, 5, 2))
print(stats())

data = [12, 4, 9, 20]
print(stats(*data))