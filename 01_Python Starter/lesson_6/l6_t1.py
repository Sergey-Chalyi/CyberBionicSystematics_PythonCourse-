# Завдання 1 

# Створіть список та введіть його значення. Знайдіть найбільший 
# та найменший елемент списку, а також суму та середнє арифметичне його значень. 
import statistics

num_list = []

for _ in range(5):
    num_list.append(int(input("Enter num: ")))

print("max =", max(num_list))
print("min =", min(num_list))
print("sum =", sum(num_list))
print("average =", statistics.mean(num_list))