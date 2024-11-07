# Завдання 3
#
# Створіть програму, яка має 2 списки цілочисельних значень та друкує
# список унікальних значень без повтору, які є в 1 списку (немає в другому) і навпаки.

num_list_1 = [i for i in range(int(input()))]
num_list_2 = [i for i in range(int(input()))]

print(list(set(num_list_1) - set(num_list_2)))

