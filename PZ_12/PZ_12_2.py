#В матрице элементы третьей строки заменить элементами из одномерного
#динамического массива соответствующей размерности.

import random

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = []
for i in range(rows):
    row = [random.randint(1, 9) for _ in range(cols)]
    matrix.append(row)

print("\nИзначальная матрица:")
for row in matrix:
    print(row)

massive = [random.randint(10, 99) for _ in range(cols)]
print("\nМассив для замены:", massive)

matrix[2] = massive

print("\nИзмененная матрица:")
for row in matrix:
    print(row)