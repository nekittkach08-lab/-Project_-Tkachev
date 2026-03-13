# Задание 29. Средствами языка Python сформировать два текстовых файла (.txt),
# содержащих по одной последовательности из целых положительных и отрицательных чисел.
# Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
#
# Элементы первого и второго файлов:
# Количество элементов первого и второго файлов:
# Количество элементов, общих для двух файлов:
# Количество четных элементов первого файла:
# Количество нечетных элементов второго файла:

# 1. Создаем два списка с целыми числами (положительными и отрицательными)
list1 = [15, -8, 23, -4, 37, 0, -12, 42, -5, 18]
list2 = [-3, 16, -8, 25, 0, 11, -4, 30, -6, 19, 100]

# 2. Записываем первый список в файл file1.txt с кодировкой UTF-8
data_str1 = ' '.join(map(str, list1))
f1 = open('file1.txt', 'w', encoding='utf-8')
f1.write(data_str1)
f1.close()

# 3. Записываем второй список в файл file2.txt с кодировкой UTF-8
data_str2 = ' '.join(map(str, list2))
f2 = open('file2.txt', 'w', encoding='utf-8')
f2.write(data_str2)
f2.close()

# 4. Создаем итоговый файл result.txt с кодировкой UTF-8
f_result = open('result.txt', 'w', encoding='utf-8')
f_result.write('Элементы первого и второго файлов: ')
f_result.write('\n')

# Читаем данные из первого файла (тоже с UTF-8)
f1 = open('file1.txt', 'r', encoding='utf-8')
first_content = f1.read()
f_result.write(first_content)
f1.close()

# Добавляем разделитель и читаем данные из второго файла
f_result.write(' : ')
f2 = open('file2.txt', 'r', encoding='utf-8')
second_content = f2.read()
f_result.write(second_content)
f2.close()
f_result.write('\n')
f_result.close()

# 5. Обработка данных
f1 = open('file1.txt', 'r', encoding='utf-8')
line1 = f1.read()
list1_nums = line1.split()
for i in range(len(list1_nums)):
    list1_nums[i] = int(list1_nums[i])
f1.close()

f2 = open('file2.txt', 'r', encoding='utf-8')
line2 = f2.read()
list2_nums = line2.split()
for i in range(len(list2_nums)):
    list2_nums[i] = int(list2_nums[i])
f2.close()

# Подсчет характеристик
count1 = len(list1_nums)
count2 = len(list2_nums)

# Общие элементы
set1 = set(list1_nums)
set2 = set(list2_nums)
common_elements = set1.intersection(set2)
common_count = len(common_elements)

# Четные элементы первого файла
even_count1 = 0
for num in list1_nums:
    if num % 2 == 0:
        even_count1 += 1

# Нечетные элементы второго файла
odd_count2 = 0
for num in list2_nums:
    if num % 2 != 0:
        odd_count2 += 1

# Дозаписываем результаты с UTF-8
f_result = open('result.txt', 'a', encoding='utf-8')
f_result.write('\n')
f_result.write(f'Количество элементов первого и второго файлов: {count1} и {count2}\n')
f_result.write(f'Количество элементов, общих для двух файлов: {common_count}\n')
f_result.write(f'Количество четных элементов первого файла: {even_count1}\n')
f_result.write(f'Количество нечетных элементов второго файла: {odd_count2}\n')
f_result.close()

print("Программа выполнена. Проверьте файлы file1.txt, file2.txt и result.txt")