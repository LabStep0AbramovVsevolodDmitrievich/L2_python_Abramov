# Задание 22
with open("example.txt", "w") as file:
    file.write("Hello, File!")

# Задание 23
with open("example.txt", "r") as file:
    print("Содержимое файла:", file.read())

# Задание 24
with open("example.txt", "a") as file:
    file.write("\nНовая строка")