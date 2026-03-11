# Список файлов
files = ['/Users/dolgoffsv/Desktop/netology/cook-book/merge/1.txt',
         '/Users/dolgoffsv/Desktop/netology/cook-book/merge/2.txt']

# Создаем списки для хранения информации
names = []        # названия файлов
counts = []       # количество строк
contents = []     # содержимое файлов

# Читаем каждый файл
for file_path in files:
    # Получаем имя файла
    if file_path == '/Users/dolgoffsv/Desktop/netology/cook-book/merge/1.txt':
        name = '1.txt'
    elif file_path == '/Users/dolgoffsv/Desktop/netology/cook-book/merge/2.txt':
        name = '2.txt'


    # Открываем и читаем файл
    f = open(file_path, 'r', encoding='utf-8')
    text = f.read()
    f.close()

    # Разбиваем текст на строки
    lines = text.split('\n')

    # Считаем количество строк
    count = len(lines)

    # Сохраняем данные
    names.append(name)
    counts.append(count)
    contents.append(lines)

# Сортируем файлы по количеству строк (от меньшего к большему)
# Проходим по всем элементам
for i in range(len(counts)):
    for j in range(i + 1, len(counts)):
        # Если нашли файл с меньшим количеством строк
        if counts[i] > counts[j]:
            # Меняем местами ВСЕ данные
            # Меняем названия
            temp = names[i]
            names[i] = names[j]
            names[j] = temp

            # Меняем количество строк
            temp = counts[i]
            counts[i] = counts[j]
            counts[j] = temp

            # Меняем содержимое
            temp = contents[i]
            contents[i] = contents[j]
            contents[j] = temp

# Создаем итоговый файл
result = open('/Users/dolgoffsv/Desktop/netology/cook-book/merge/result_merge.txt', 'w', encoding='utf-8')

# Записываем данные
for i in range(len(names)):
    # Имя файла
    result.write(names[i] + '\n')
    # Количество строк
    result.write(str(counts[i]) + '\n')
    # Содержимое файла
    for line in contents[i]:
        result.write(line + '\n')

# Закрываем файл
result.close()

print("Готово! Файлы объединены в result_merge.txt")
print("Служебная информация:")
for i in range(len(names)):
    print(names[i], '-', counts[i], 'строк')