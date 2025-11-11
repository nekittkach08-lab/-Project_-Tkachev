#Даны положительные числа A, B, C. На прямоугольнике размера A х B размещено
#максимально возможное количество квадратов со стороной C (без наложений).
#Найти количество квадратов, размещенных на прямоугольнике. Операции
#умножения и деления не использовать.

def multiply_without_op(x, y):
    result = 0
    for _ in range(y):
        result += x
    return result

def div_without_op(x, y):
    count = 0
    sum_y = 0
    while sum_y + y <= x:
        sum_y += y
        count += 1
    return count

# Вводим значения:
try:
    A = float(input("Введите длину прямоугольника A (положительное число): "))
    B = float(input("Введите ширину прямоугольника B (положительное число): "))
    C = float(input("Введите сторону квадрата C (положительное число): "))
except ValueError:
    print("Ошибка: введено не числовое значение.")
    exit()

# Проверка, что числа положительные
if A <= 0 or B <= 0 or C <= 0:
    print("Ошибка: все числа должны быть положительными.")
    exit()

# Переводим к целым числам для работы
A_int = int(A)
B_int = int(B)
C_int = int(C)

# Проверка, что стороны квадрата не больше размеров прямоугольника
if C_int > A_int or C_int > B_int:
    print("Квадрат со стороной C не помещается на прямоугольник.")
    exit()

# Расчёт количества квадратов вдоль каждой стороны
count_along_A = div_without_op(A_int, C_int)
count_along_B = div_without_op(B_int, C_int)

# Если ни одного квадрата разместить нельзя
if count_along_A == 0 or count_along_B == 0:
    print("Невозможно разместить ни одного квадрата со стороной C.")
    exit()

# Общее количество
total_squares = multiply_without_op(count_along_A, count_along_B)

print("Максимальное количество размещённых квадратов:", total_squares)