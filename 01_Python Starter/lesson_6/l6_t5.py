# Завдання 5

# Створіть список натуральних чисел int_list. Кожне непарне 
# значення списку додайте до нового списку new_list. Користувач 
# вводить з клавіатури кількість повторів списку repeat. Здійсніть 
# дублювання списку new_list, repeat кількість разів. Очистіть список int_list. 

int_list = [int(input("Enter num: ")) for _ in range(5)]
print('int_list =', int_list)

new_list = [el for el in int_list if el % 2 != 0]
print('new_list =', new_list)

repeat_count = int(input("Enter count of repeated: "))

new_list_copy = new_list.copy()
print("new_list_copy", new_list_copy)

new_list_repeats = new_list * repeat_count
print("new_list_repeats", new_list_repeats)

int_list.clear()
print("int_list.clear", int_list)