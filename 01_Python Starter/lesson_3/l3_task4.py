# Завдання 4

# Напишіть програму-калькулятор, в якій користувач зможе обрати операцію, ввести необхідні числа та отримати результат. Операції, які необхідно реалізувати: додавання, віднімання, множення, ділення, зведення в ступінь, квадратний корінь, кубічний корінь, синус, косинус та тангенс числа. 


import math

n1 = int(input("Enter num1: "))
n2 = int(input("Enter num2: "))
action = input("Enter action to do (+, -, *, /, ^, sqrt, cbrt, sin, cos, tan): ")

match action:
    case "+":
        result = n1 + n2
        print(f"Result: {result}")
    case "-":
        result = n1 - n2
        print(f"Result: {result}")
    case "*":
        result = n1 * n2
        print(f"Result: {result}")
    case "/":
        if n2 != 0:
            result = n1 / n2
            print(f"Result: {result}")
        else:
            print("Error: Division by zero!")
    case "^":
        result = n1 ** n2
        print(f"Result: {result}")
    case "sqrt":
        result = math.sqrt(n1)
        print(f"Square root of {n1}: {result}")
    case "cbrt":
        result = n1 ** (1/3)
        print(f"Cubic root of {n1}: {result}")
    case "sin":
        result = math.sin(math.radians(n1))
        print(f"Sin({n1}°): {result}")
    case "cos":
        result = math.cos(math.radians(n1))
        print(f"Cos({n1}°): {result}")
    case "tan":
        result = math.tan(math.radians(n1))
        print(f"Tan({n1}°): {result}")
    case _:
        print("Invalid action")
