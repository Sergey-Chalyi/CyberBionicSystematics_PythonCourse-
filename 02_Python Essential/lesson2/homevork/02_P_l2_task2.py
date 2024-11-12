# Завдання 2

# Опишіть класи графічного об'єкта, прямокутника та об'єкта, який може 
# обробляти натискання миші. Опишіть клас кнопки. Створіть об'єкт кнопки 
# та звичайного прямокутника. Викличте метод натискання на кнопку.

class GraphicObject:
    pass

class Rectangular:
    pass

class MousePushObject:
    def push(self):
        print('Pushed on the button')

class Button(GraphicObject, MousePushObject, Rectangular):
    pass

button = Button()
rectangular = Rectangular()

button.push()
# rectangular.push_on_button()