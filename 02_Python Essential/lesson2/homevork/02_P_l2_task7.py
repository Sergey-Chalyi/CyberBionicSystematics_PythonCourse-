# Завдання 7

# Створіть ієрархію класів транспортних засобів. 
# У загальному класі опишіть загальні всім транспортних засобів поля, 
# у спадкоємцях – специфічні їм. Створіть кілька екземплярів. 
# Виведіть інформацію щодо кожного транспортного засобу.

class Vehicle:
    def __init__(self, brand: str, model: str, year: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self) -> str:
        return f"{self.year} {self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand: str, model: str, year: int, doors: int) -> None:
        super().__init__(brand, model, year)
        self.doors = doors

    def get_info(self) -> str:
        return f"{super().get_info()}, Doors: {self.doors}"

class Motorcycle(Vehicle):
    def __init__(self, brand: str, model: str, year: int, engine_volume: float) -> None:
        super().__init__(brand, model, year)
        self.engine_volume = engine_volume

    def get_info(self) -> str:
        return f"{super().get_info()}, Engine Volume: {self.engine_volume}L"

class Bicycle(Vehicle):
    def __init__(self, brand: str, model: str, year: int, has_gears: bool) -> None:
        super().__init__(brand, model, year)
        self.has_gears = has_gears

    def get_info(self) -> str:
        gears_info = "Yes" if self.has_gears else "No"
        return f"{super().get_info()}, Has Gears: {gears_info}"

# Создаем экземпляры каждого класса
car = Car("Toyota", "Camry", 2020, 4)
motorcycle = Motorcycle("Yamaha", "MT-07", 2021, 0.7)
bicycle = Bicycle("Giant", "Escape 3", 2019, True)

# Выводим информацию о каждом транспортном средстве
print(car.get_info())
print(motorcycle.get_info())
print(bicycle.get_info())
