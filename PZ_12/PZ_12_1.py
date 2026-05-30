#В матрице элементы последнего столбца заменить на -1.

import random

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

# функциональное создание матрицы
matrix = list(map(lambda _: [random.randint(1, 9) for _ in range(cols)], range(rows)))

print("\nИзначальная матрица:")
for row in matrix:
    print(row)

for row in matrix:
    row[-1] = -1

print("\nИзмененная матрица:")
for row in matrix:
    print(row)