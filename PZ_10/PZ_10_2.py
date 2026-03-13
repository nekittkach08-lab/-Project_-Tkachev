# Задача 2. Из предложенного текстового файла (text18-29.txt) вывести на экран
# его содержимое, количество символов в тексте. Сформировать новый файл,
# в который поместить текст в стихотворной форме предварительно поставив
# последнюю строку между второй и третьей.

file_name = 'text18-29.txt'

try:
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    full_text = ''.join(lines)
    char_count = len(full_text)

    print(f"Количество символов в тексте (включая пробелы и знаки препинания): {char_count}")
    print()

    if len(lines) >= 3:
        last_line = lines[-1]

        lines.pop()

        lines.insert(2, last_line)

        print("Текст после перестановки последней строки между второй и третьей:")
        print("------------------------------------------------------------------")
        for line in lines:
            print(line, end='')
        print("------------------------------------------------------------------")

        # 5. Записываем результат в новый файл
        new_file_name = 'text18-29_modified.txt'
        with open(new_file_name, 'w', encoding='utf-8') as new_file:
            new_file.writelines(lines)

        print(f"Результат сохранен в файл: {new_file_name}")

    else:
        print("В файле недостаточно строк для выполнения перестановки.")

except FileNotFoundError:
    print(f"Ошибка: Файл '{file_name}' не найден!")
except Exception as e:
    print(f"Произошла ошибка: {e}")