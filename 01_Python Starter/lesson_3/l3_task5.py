# Завдання 5

# Напишіть програму для перевірки введеного числа на ознаку парності. Якщо число парне/непарне – вивести відповідне повідомлення на екран. Для опису цього алгоритму використовувати тернарний оператор. 

num = int(input("Enter number: "))
print("even number" if num % 2 == 0 else "odd number")