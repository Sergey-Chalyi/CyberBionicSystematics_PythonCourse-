# Завдання 4

# Напишіть програму, в якій користувач вводить фразу з клавіатури, яка складається з 10 символів. На екрані виведіть суму ASCII-кодів символів введеного рядка. 

phrase = input()

print(sum(ord(char) for char in phrase))
