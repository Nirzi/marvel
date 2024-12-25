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
print("Фильтрованный словарь по ID:")
pprint(filtered_dict)

#Создайте множество уникальных значений ключа 'director'
directors_set = {value['director'] for value in full_dict.values() if 'director' in value}

print("Множество режиссёров:")
print(directors_set)

#Копия словаря, где 'year' преобразован в строку
transformed_dict = {
    key: {**value, 'year': str(value['year'])} for key, value in full_dict.items()
}