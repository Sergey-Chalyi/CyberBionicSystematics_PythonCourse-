# Завдання 4

# Ознайомтеся за допомогою документації з класами namedtuple та 
# deque модуля collections. Створіть фабрику іменованих кортежів оцінок 
# для учнів однієї групи з предметів: алгебра, геометрія, історія, 
# інформатика, географія. Вивести дані на екран.

from collections import namedtuple

Schoolkid = namedtuple("Schoolkid", "algebra geometry history computer_science geography")

# Создаем дополнительных учеников с оценками по 12-балльной системе
person1 = Schoolkid(algebra=12, geometry=10, history=11, computer_science=12, geography=9)
person2 = Schoolkid(algebra=8, geometry=7, history=9, computer_science=10, geography=6)
person3 = Schoolkid(algebra=11, geometry=12, history=10, computer_science=9, geography=12)
person4 = Schoolkid(algebra=5, geometry=6, history=7, computer_science=8, geography=4)

print(person1)
print(person2)
print(person3)
print(person4)
