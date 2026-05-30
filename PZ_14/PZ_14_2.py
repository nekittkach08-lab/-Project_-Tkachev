#Дано целое число N (>0). Найти произведение 1.1 • 1.2 • 1.3 •... (N сомножителей).

import tkinter as tk
from tkinter import messagebox

def func(N):
    kol = 1.0
    for k in range(1, N + 1):
        kol *= (1 + k / 10)
    return kol

def calculate():
    try:
        N = int(entry.get())
        if N <= 0:
            messagebox.showerror("Ошибка", "N должно быть больше 0")
            return
        result = func(N)
        result_label.config(text=f"Результат: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите целое число")

# создание окна
root = tk.Tk()
root.title("Произведение последовательности")
root.geometry("350x200")

# элементы интерфейса
label = tk.Label(root, text="Введите N (>0):")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Вычислить", command=calculate)
button.pack(pady=10)

result_label = tk.Label(root, text="Результат: ")
result_label.pack(pady=10)

# запуск приложения
root.mainloop()