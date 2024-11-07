# Завдання 3

# Простим називається число, яке ділиться націло лише на 
# одиницю і на саме себе. Число 1 не вважається простим. 
# Напишіть програму, яка знаходить усі прості числа в 
# заданому проміжку, виводить їх на екран, а потім на 
# вимогу користувача виводить їхню суму або добуток.

import math


sequence_start = int(input("Enter sequence start:"))
sequence_finish = int(input("Enter sequence finish:"))

final_num_list = []
for num in range(sequence_start, sequence_finish + 1):
    if num == 1:
        continue
    if num in [2, 3, 5, 7]:
        final_num_list.append(num)
        continue
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        continue
    else:
        final_num_list.append(num)
print("All simple nums in the sequence:", final_num_list)

if input("Do you want to see sum or multiplication of this sequence (yes/no)? ") == 'yes':
    if input("Do you want to see sum (yes/no)? ") == "yes":
        print('sum =', sum(final_num_list))
    if input("Do you want to see multiplication (yes/no)? ") == "yes":
        print('multiplication =', math.prod(final_num_list))

