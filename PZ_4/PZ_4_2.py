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

try:
    A = float(input("Введите A: "))
    B = float(input("Введите B: "))
    C = float(input("Введите C: "))

    # Проверка на положительность входных данных
    if A <= 0 or B <= 0 or C <= 0:
        print("Все числа должны быть положительными.")
    else:
        A_int = int(A)
        B_int = int(B)
        C_int = int(C)

        if C_int > A_int or C_int > B_int:
            print("Квадрат со стороной C не поместится на прямоугольник.")
        else:
            count_A = div_without_op(A_int, C_int)
            count_B = div_without_op(B_int, C_int)
            total = multiply_without_op(count_A, count_B)
            print("Максимальное количество квадратов:", total)

except ValueError:
    print("Ошибка ввода: пожалуйста, введите числовые значения.")
