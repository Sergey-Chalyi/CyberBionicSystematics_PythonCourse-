# Завдання 4

# Створіть клас, який описує автомобіль. Створіть клас автосалону, 
# що містить в собі список автомобілів, доступних для продажу, 
# і функцію продажу заданого автомобіля.

class Car:
    def __init__(self, model: str, year: int, max_speed: int, cost: int) -> None:
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.cost = cost
    
    def __str__(self):
        return f"{self.model}, {self.year}, Max Speed: {self.max_speed} km/h, Cost: ${self.cost}"


class CarShowroom:
    def __init__(self) -> None:
        self.car_list = []

    def add_car(self, car: Car) -> None: 
        self.car_list.append(car)
    
    def sell_car(self, car: Car) -> bool:
        if car in self.car_list: 
            self.car_list.remove(car)
            return True
        else:
            return False