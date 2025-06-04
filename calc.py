while True:
    try:
        expression = input("Введите выражение (например 2 + 2) или 'выход' для завершения: ")
        if expression.lower() == 'выход':
            break
        
        parts = expression.split()
        if len(parts) != 3:
            print("Ошибка: неверный формат ввода")
            continue
            
        a = float(parts[0])
        op = parts[1]
        b = float(parts[2])
        
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b == 0:
                print("Ошибка: деление на ноль")
                continue
            result = a / b
        else:
            print("Ошибка: неизвестная операция")
            continue
            
        print(f"Результат: {result}")
        
    except ValueError:
        print("Ошибка: введены не числа")
    except Exception as e:
        print(f"Произошла ошибка: {e}")