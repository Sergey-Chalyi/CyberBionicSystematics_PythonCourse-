# Завдання 6

# Використовуючи код example_10, створіть класовий метод 
# (для створення використовуйте декоратор @classmethod).
# Метод має підраховувати кількість об'єктів цього класу які досягли повноліття, 
# для вирішення задачі використовуйте статичний метод створенний в завданні 5

class Human:
    adult_count = 0

    def __init__(self, age: int) -> None:
        self.age = age
        if Human.is_adult(age):
            Human.adult_count += 1
    
    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18

    @classmethod
    def get_adult_count(cls) -> int:
        return cls.adult_count

print(Human.get_adult_count())

human1 = Human(18)
print(Human.get_adult_count())
human1 = Human(22)
print(Human.get_adult_count())
human1 = Human(10)
print(Human.get_adult_count())

