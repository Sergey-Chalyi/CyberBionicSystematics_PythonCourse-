# Завдання 5

# Використовуючи код example_10, створіть статичний метод класу  
# ( для створення використовуйте декоратор @staticmethod ), 
# метод має приймати вік людини та перевіряти чи досягла вона 
# повноліття, метод має повертати True або False

class Human:
    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18
    
print(Human.is_adult(18))
print(Human.is_adult(10))
print(Human.is_adult(20))