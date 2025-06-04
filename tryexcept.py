# Задание 25
try:
    num = int(input("Введите число: "))
    print(f"Вы ввели: {num}")
except ValueError:
    print("Ошибка: введено не число")

# Задание 26
try:
    with open("nonexistent.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Ошибка: файл не существует")