# Завдання 2

# Напишіть програму, в якій користувач вводить із клавіатури діапазон чисел 
# (в діапазоні має бути не менше 5 чисел). Вивести на екран суму другого, передостаннього, 
# а також середнього арифметичного значення даної послідовності. 
import statistics

my_nums = []

for _ in range(5):
    my_nums.append(int(input("Enter number: ")))

print("The second element =", my_nums[1])
print("The penultimate number =", my_nums[len(my_nums) - 2])
print("Arithmetic mean =", statistics.mean(my_nums))