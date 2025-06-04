import random
import datetime
import math

# Задание 27
print("Случайное число:", random.randint(1, 100))

# Задание 28
print("Текущая дата и время:", datetime.datetime.now())

# Задание 29
def sqrt_without_math(n):
    return n ** 0.5

num = float(input("Введите число: "))
print(f"Квадратный корень (math): {math.sqrt(num)}")
print(f"Квадратный корень (без math): {sqrt_without_math(num)}")