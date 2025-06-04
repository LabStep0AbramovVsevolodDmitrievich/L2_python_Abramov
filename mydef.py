# Задание 19
def add_numbers(a, b):
    return a + b

print("Сумма 5 и 3:", add_numbers(5, 3))

# Задание 20
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Введите число для проверки: "))
print("Простое" if is_prime(num) else "Не простое")

# Задание 21
def average(numbers):
    return sum(numbers) / len(numbers)

nums = [1, 2, 3, 4, 5]
print(f"Среднее: {average(nums)}")