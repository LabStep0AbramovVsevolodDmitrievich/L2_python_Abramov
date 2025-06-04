import random

def guess_number():
    secret = random.randint(0, 10)
    attempts = 3
    
    print("Я загадал число от 0 до 10. У тебя 3 попытки!")
    
    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Попытка {attempt}. Твой вариант: "))
            
            if guess == secret:
                print("Поздравляю! Ты угадал!")
                return
            elif guess < secret:
                print("Не верно! Загаданное число больше!")
            else:
                print("Не верно! Загаданное число меньше!")
                
        except ValueError:
            print("Пожалуйста, вводи только числа!")
    
    print(f"Ты проиграл! Я загадал число {secret}.")

guess_number()