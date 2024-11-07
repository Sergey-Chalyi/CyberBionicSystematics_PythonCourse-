# Завдання 1

# Створіть програму, яка зчитує рядок, в якому знаходиться ПІБ користувача 
# і перевіряє, чи складається рядок з літер, при чому кожне слово має бути записане з великої літери. Вивести результат на екран.



full_name = input("Enter your full name: ")
name_list = full_name.split()

while True:
    flag = True
    for name in name_list:
        if not name.isalpha() or not name.istitle():
            flag = False
            break 

    if not flag:
        print("All words need to start with a capital letter")
        full_name = input("Enter your full name: ")
        name_list = full_name.split()
        continue
    
    print("Your full name - " + full_name)
    break   
    
