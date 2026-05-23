#Составить генератор (yield), который преобразует все буквенные символы в
#строчные.

def to_lowercase_generator(text):
    for char in text:
        yield char.lower()

string = "ПРИВЕТ, МИР!"
gen = to_lowercase_generator(string)

result = "".join(gen)
print(result)
