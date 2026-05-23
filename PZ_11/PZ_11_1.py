#Организовать и вывести последовательность на N произвольных целых
#элементов, сформировать новую последовательность куда поместить положительные
#четные элементы, найти их сумму и среднее арифметическое.

import random


N = 10
random1 = random.sample(range(-100, 101), N)
print(f"Последовательность: {random1}")

random_new = [x for x in random1 if x > 0 and x % 2 == 0]
print(f"Новая последовательность: {random_new}")

if random_new:
    total_sum = sum(random_new)
    sredneye = total_sum / len(random_new)

    print(f"Сумма всех элементов: {total_sum}")
    print(f"Среднее арифметическое: {sredneye:.2f}")
else:
    print("Подходящих элементов не найдено")
