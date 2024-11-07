# Створіть програму "Шкільний журнал" користувач заповнює журнал учнями 
# а саме ім'я та прізвища, допоки не введе "стоп". Об'єднайте всіх учнів 
# в кортеж. За допомогою циклу for та enumerate виведіть на екран 
# пронумерований список унів у першого учня має бути номер 1

class_names = tuple()

name = input("Enter name: ")

while name != 'stop':
    class_names += (name,)
    name = input("Enter name: ")

for index, name in enumerate(class_names):
    print(index + 1, name) 

