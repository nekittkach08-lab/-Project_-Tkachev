#Дан список A размера N и целое число K (1 < K < N). Преобразовать список,
#увеличив каждый его элемент на исходное значение элемента AK.

import random

N = 10
A = [random.randint(0, 100) for _ in range(N)]
print("Исходный список:", A)

K = random.randint(2, N - 2)
print("K =", K)
value = A[K]
print("Значение A[K]:", value)

for i in range(N):
    A[i] += value

print("Измененный список:", A)