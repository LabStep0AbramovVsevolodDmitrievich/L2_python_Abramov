# Задание 10
print("Числа от 1 до 10:")
for i in range(1, 11):
    print(i, end=' ')
print()

# Задание 11
n = int(input("Введите N: "))
for i in range(1, n+1):
    print(i, end=' ')
print()

# Задание 12
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(f"Сумма чисел от 1 до 100: {total}")