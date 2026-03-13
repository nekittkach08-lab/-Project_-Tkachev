# Задача 2. Из предложенного текстового файла (text18-29.txt) вывести на экран
# его содержимое, количество символов в тексте. Сформировать новый файл,
# в который поместить текст в стихотворной форме предварительно поставив
# последнюю строку между второй и третьей.
# Задача 2. Из предложенного текстового файла (text18-29.txt) вывести на экран
# его содержимое, количество символов в тексте. Сформировать новый файл,
# в который поместить текст в стихотворной форме предварительно поставив
# последнюю строку между второй и третьей.

with open('text18-29.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

full_text = "".join(lines)
print("Содержимое файла:")
print(full_text)
print(f"\nКоличество символов: {len(full_text)}")

clean_lines = [line.strip() for line in lines if line.strip()]

if len(clean_lines) >= 3:
    last_line = clean_lines.pop()
    clean_lines.insert(2, last_line)

with open('new_text.txt', 'w', encoding='utf-8') as f:
    for line in clean_lines:
        f.write(line + '\n')

print("\nНовый файл 'new_text.txt' успешно создан.")
