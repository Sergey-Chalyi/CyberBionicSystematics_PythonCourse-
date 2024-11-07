# Завдання 4
#
# Створіть магазин канцтоварів використовуючи списки для зберігання елементів.
# Для додавання елементів створіть функцію, яка буде запитувати дані в користувача
# і зібрані дані у вигляді кортежу додавати у створений список на початку.
# Результат вивести на екран. Під час створення дотримуйтесь правил специфікації PEP 8.

def add_office_supplies():
    """
    Function to add items to the office supplies list
    """
    office_supplies_list = []
    while True:
        name = input("Enter item name: ")
        price = float(input("Enter price: "))
        amount = int(input("Enter quantity: "))
        office_supplies_list.append((name, price, amount))
        choice = input("Continue adding? (y/n): ")
        if choice.lower() != "y":
            break
    return office_supplies_list