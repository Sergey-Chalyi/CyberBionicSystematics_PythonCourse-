# Завдання 1
# Дано два рядки. Виведіть на екран символи, які є в обох рядках.

str1 = input()
str2 = input()

print(set(str1).intersection(set(str2)))