# Задача №1
cook_book = {}

with open('recipes/recipes.txt', 'r', encoding='utf-8') as file:
    # Читаем все строки и убираем пустые
    lines = []
    for line in file:
        line = line.strip()
        if line:  # если строка не пустая
            lines.append(line)

# Обрабатываем строки
i = 0
while i < len(lines):
    # Название блюда
    dish_name = lines[i]
    i += 1

    # Количество ингредиентов
    ingredients_count = int(lines[i])
    i += 1

    # Список ингредиентов для блюда
    ingredients = []
    for _ in range(ingredients_count):
        # Разделитель строки символом - |
        parts = lines[i].split('|')
        ingredient = {
            'ingredient_name': parts[0].strip(),
            'quantity': int(parts[1].strip()),
            'measure': parts[2].strip()
        }
        ingredients.append(ingredient)
        i += 1

    # Добавляем блюдо в словарь
    cook_book[dish_name] = ingredients

# Вывод результата
print("cook_book = {")
for dish, ingredients in cook_book.items():
    print(f"  '{dish}': [")
    for ing in ingredients:
        print(f"    {{'ingredient_name': '{ing['ingredient_name']}', 'quantity': {ing['quantity']}, 'measure': '{ing['measure']}'}},")
    print("    ],")
print("}")


# Задача №2
cook_book = {}

with open('recipes/recipes.txt', 'r', encoding='utf-8') as file:
    # Читаем все строки и убираем пустые
    lines = []
    for line in file:
        line = line.strip()
        if line:  # Если строка не пустая
            lines.append(line)

# Обрабатываем строки
i = 0
while i < len(lines):
    # Название блюда
    dish_name = lines[i]
    i += 1

    # Количество ингредиентов
    ingredients_count = int(lines[i])
    i += 1

    # Список ингредиентов для блюда
    ingredients = []
    for _ in range(ingredients_count):
        # Разделитель строки символом - |
        parts = lines[i].split('|')
        ingredient = {
            'ingredient_name': parts[0].strip(),
            'quantity': int(parts[1].strip()),
            'measure': parts[2].strip()
        }
        ingredients.append(ingredient)
        i += 1

    # Добавляем блюдо в словарь
    cook_book[dish_name] = ingredients
# Функция получения списка покупок
def get_shop_list_by_dishes(dishes, person_count):
    """
    Принимает список блюд и количество персон
    Возвращает словарь с ингредиентами
    """
    shop_list = {}

    # Перебираем все блюда из списка
    for dish in dishes:
        # Проверяем, есть ли такое блюдо в cook_book
        if dish in cook_book:
            # Перебираем ингредиенты для этого блюда
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                # Если ингредиент есть в списке, добавляем количество
                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    # если ингредиента нет в списке, создаем новую запись
                    shop_list[name] = {'measure': measure, 'quantity': quantity}

    return shop_list

# Проверяем функцию
result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 4)

# Выводим результат
print("{")
for ingredient, data in result.items():
    print(f"  '{ingredient}': {{'measure': '{data['measure']}', 'quantity': {data['quantity']}}},")
print("}")