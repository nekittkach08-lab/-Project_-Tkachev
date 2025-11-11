#Дано целое число N (>0). Найти произведение 1.1 • 1.2 • 1.3 •... (N сомножителей).

def func(N):
    kol = 1.0
    for k in range(1, N + 1):
        kol *= (1 + k / 10)
    return kol

try:
    N = int(input("Введите целое число N (>0): "))
    if N <= 0:
        print("Ошибка: N должно быть больше 0.")
    else:
        result = func(N)
        print("Результат:", result)
except ValueError:
    print("Ошибка: введено не целое число.")