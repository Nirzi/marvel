from marvel import full_dict
from pprint import pprint


#Реализуйте ввод от пользователя
user_input = input("Введите ID через пробел: ")

#Преобразование строки в список чисел
ids = list(map(lambda x: int(x) if x.isdigit() else None, user_input.split()))

# Результат обработки списка ID
print("Список ID после обработки:", ids)

filtered_dict = {
    key: value for key, value in full_dict.items() if key in ids
}

# Результат фильтрации
print()
print()
print()
print()
print()
print("Фильтрованный словарь по ID:")
pprint(filtered_dict)

#Создайте множество уникальных значений ключа 'director'
directors_set = {value['director'] for value in full_dict.values() if 'director' in value and value['director']}

print()
print()
print()
print()
print()
print("Множество режиссёров:")
print(directors_set)

#Копия словаря, где 'year' преобразован в строку
transformed_dict = {
    key: {**value, 'year': str(value['year'])} for key, value in full_dict.items()
}

movies_starting_with_Ч = {
    key: value for key, value in full_dict.items() if value['title'] and value['title'].startswith('Ч')
}

# Результат фильтрации
print()
print()
print()
print()
print()
print("Фильмы, начинающиеся на букву 'Ч':")
pprint(movies_starting_with_Ч)

#Сортировка по одному параметру (например, 'year')
sorted_by_year = dict(sorted(full_dict.items(), key=lambda item: item[1]['year'] if isinstance(item[1]['year'], int) else 0))

# Результат сортировки
print()
print()
print()
print()
print()
print("Словарь, отсортированный по году:")
pprint(sorted_by_year)


#Сортировка по двум параметрам (например, 'stage' и 'year')
sorted_by_stage_and_year = dict(sorted(
    full_dict.items(),
    key=lambda item: (item[1]['stage'], item[1]['year']) if isinstance(item[1]['year'], int) else (item[1]['stage'], 0)
))

# Результат сортировки
print()
print()
print()
print()
print()
print("Словарь, отсортированный по фазе и году:")
pprint(sorted_by_stage_and_year)

#Однострочник для фильтрации и сортировки
filtered_and_sorted = dict(sorted(
    filter(lambda item: item[1]['title'] and item[1]['title'].startswith('М'), full_dict.items()),
    key=lambda item: item[1]['year'] if isinstance(item[1]['year'], int) else 0
))

# Результат однострочника
print()
print()
print()
print()
print()
print("Фильтрованный и отсортированный словарь:")
pprint(filtered_and_sorted)