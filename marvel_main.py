from marvel import full_dict
from pprint import pprint


# Шаг 1: Реализуйте ввод от пользователя
user_input = input("Введите ID через пробел: ")

# Шаг 2: Преобразование строки в список чисел, замена нечисловых элементов на None
ids = list(map(lambda x: int(x) if x.isdigit() else None, user_input.split()))

# Результат обработки списка ID
print("Список ID после обработки:", ids)