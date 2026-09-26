rows = 6
triangle = []

for i in range(rows):
    row = []
    for j in range(i + 1):
        if j == 0 or j == i:
            row.append(1)
        else:
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
    triangle.append(row)

for row in triangle:
    print(' '.join(f'{value:3}' for value in row).center(40))