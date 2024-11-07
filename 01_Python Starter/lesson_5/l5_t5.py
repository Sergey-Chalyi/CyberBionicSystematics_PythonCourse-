# Завдання 5

# Напишіть програму, яка вводить з клавіатури послідовність чисел, 
# перетворює послідовність на кортеж і виводить його відсортованим у порядку зростання. 


nums = tuple(int(input("Enter num: ")) for _ in range(5))

sorted_nums = tuple(sorted(nums))
print(sorted_nums)