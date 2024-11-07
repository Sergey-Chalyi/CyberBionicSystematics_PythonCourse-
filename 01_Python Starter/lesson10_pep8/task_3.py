# Завдання 3
#
# Створіть інженерний калькулятор з використанням модуля math,
# в якому передбачене меню. Під час створення дотримуйтесь правил специфікації PEP 8.

import math

def menu():
    """Меню інженерного калькулятора"""
    print("1. Синус")
    print("2. Косинус")
    print("3. Тангенс")
    print("4. Арксинус")
    print("5. Арккосинус")
    print("6. Арктангенс")
    print("7. Вихід")

def main():
    """Головна функція інженерного калькулятора"""
    while True:
        menu()
        choice = input("Введіть номер пункту меню: ")
        if choice == "1":
            angle = float(input("Введіть кут в градусах: "))
            print("Синус: ", math.sin(math.radians(angle)))
        elif choice == "2":
            angle = float(input("Введіть кут в градусах: "))
            print("Косинус: ", math.cos(math.radians(angle)))
        elif choice == "3":
            angle = float(input("Введіть кут в градусах: "))
            print("Тангенс: ", math.tan(math.radians(angle)))
        elif choice == "4":
            angle = float(input("Введіть кут в градусах: "))
            print("Арксинус: ", math.asin(math.radians(angle)))
        elif choice == "5":
            angle = float(input("Введіть кут в градусах: "))
            print("Арккосинус: ", math.acos(math.radians(angle)))
        elif choice == "6":
            angle = float(input("Введіть кут в градусах: "))
            print("Арктангенс: ", math.atan(math.radians(angle)))
        elif choice == "7":
            break
        else:
            print("Вибачте, такого пункту меню не існує")

if __name__ == "__main__":
    main()