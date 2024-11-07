# Завдання 6

# Для цього завдання вихідний список значень беремо з 
# підсумкового списку new_list завдання 5. Користувач вводить 
# з клавіатури значення; якщо таке є у цьому списку — 
# вивести кількість його повторів та його позицію у цьому списку.

int_list = [1, 2, 3, 4, 5]

user_value_to_find = int(input("Enter value to find in the list: "))

if user_value_to_find in int_list:
    print((
        f"The value [{user_value_to_find}] is contained in the list "
        f"[{int_list.count(user_value_to_find)}] times "
        f"on positions {[i for i in range(len(int_list)) if int_list[i] == user_value_to_find]}"
    ))

