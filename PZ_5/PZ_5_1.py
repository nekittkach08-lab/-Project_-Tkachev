#Составить функцию, которая напечатает сорок любых символов

import random

def print_40_sym():
    symbols = "dgfdgcfnekrzxwlaeuuidflu2346875o3xp0t45b.506.x3q745z46cv6b7589673xw464563wq475ctrlgtvisxtxrlg"
    result = ''.join(random.choice(symbols) for _ in range(40))
    print(result)

print_40_sym()





