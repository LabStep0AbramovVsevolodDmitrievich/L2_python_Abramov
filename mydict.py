# Задание 16
student = {
    "имя": "Иван",
    "возраст": 20,
    "курс": 2
}
print("Информация о студенте:", student)

# Задание 17
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print("Объединенный словарь:", merged)

# Задание 18
key = input("Введите ключ для проверки: ")
print("Ключ есть в словаре" if key in student else "Ключа нет в словаре")