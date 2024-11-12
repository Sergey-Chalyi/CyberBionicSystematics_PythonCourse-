# Завдання 3

# Створіть ієрархію класів із використанням множинного успадкування. 
# Виведіть на екран порядок вирішення методів для кожного класу. 
# Поясніть, чому лінеаризація даних класів виглядає саме так.

class Animal:
    def breath(self):
        pass
    
    def move(self):
        pass

class Mammals(Animal): # ссавці
    def jump(self):
        pass

class MindAbilities:
    def think(self):
        pass

class Dog(Mammals, MindAbilities):
    def make_sound(self):
        pass

print("Animal MRO:", Animal.__mro__)
print("Mammals MRO:", Mammals.__mro__)
print("MindAbilities MRO:", MindAbilities.__mro__)
print("Dog MRO:", Dog.__mro__)





