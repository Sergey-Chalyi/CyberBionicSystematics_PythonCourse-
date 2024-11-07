# Завдання 5

# Напишіть програму, яка вводить з клавіатури текст і виводить його в оберненому порядку.

start_str = input("Enter your text with 10 characters: ")

print("result: ", end='')
print(
    start_str[9], 
    start_str[8], 
    start_str[7], 
    start_str[6], 
    start_str[5], 
    start_str[4], 
    start_str[3], 
    start_str[2], 
    start_str[1], 
    start_str[0], 
    sep=''
)