#В исходном текстовом файле(hotline1.txt) найти все номера телефонов,
#соответствующих шаблону 8(000)000-00-00. Посчитать количество полученных
#элементов. После фразы «Горячая линия» добавить фразу «Министерства
#образования Ростовской области», выполнив манипуляции в новом файле.

import re

file = open('hotline.txt', 'r', encoding="utf-8")
text = file.read()
file.close

pattern = r"8\d{10}"
numbers = re.findall(pattern, text)

print("Найденные номера:")
print("\n".join(numbers))

count = len(numbers)
print(f'Количество полученных номеров: {count}')

old = "Горячая линия"
new = "«Горячая линия» Министерства образования Ростовской области"

upd_text = text.replace(old, new)
file_out = open('hotline_upd.txt', 'w', encoding="utf-8")
file_out.write(upd_text)
file_out.close()
print("Готово! Изменения сохранены в файл 'hotline_updated.txt'")