#Дан символ C и строки S, S0. Перед каждым вхождением символа C в строку S
#вставить строку S0.

import random
import string

S = ''.join(random.choice(string.ascii_letters) for _ in range(15))
C = random.choice(string.ascii_letters)
S0 = 'S0'

result = ''
for ch in S:
    if ch == C:
        result += S0
    result += ch

print("S:", S)
print("C:", C)
print("S0:", S0)
print("Результат:", result)