#На числовой оси расположены три точки: A, B, C. Определить, какая из двух
#последних точек (B или C) расположена ближе к A, и вывести эту точку и ее
#расстояние от точки A.

A = float(input("A = "))
B = float(input("B = "))
C = float(input("C = "))

d1 = abs(A - B)
d2 = abs(A - C)

if d1 < d2:
    print(f"B {d1}")
elif d2 < d1:
    print(f"C {d2}")
else:
    print(f"Одинаково {d1}")