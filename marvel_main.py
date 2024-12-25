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
directors_set = {value['director'] for value in full_dict.values() if 'director' in value}

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

# Шаг 7: Сортировка по одному параметру (например, 'year')
sorted_by_year = dict(sorted(full_dict.items(), key=lambda item: item[1]['year'] if isinstance(item[1]['year'], int) else 0))

# Результат сортировки
print()
print()
print()
print()
print()
print("Словарь, отсортированный по году:")
pprint(sorted_by_year)