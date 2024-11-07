# Task 1
# Створіть пустий список. Створіть функціонал де користувач вводить числа допоки не введе слово "Stop" всі числа які ввів користувач додайте в створений раніше список. Після того як користувач завершив введення даних переберіть список та виведіть на екран лише числа які більше 10

# num_list = []
# user_input = input("Enter your number: ")
# while user_input != 'Stop':
#     num_list.append(int(user_input))
#     user_input = input("Enter your number: ")

# print(*[el for el in num_list if int(el) > 10])

#----------------------------------
# Task 2
# Створіть пустий список учнів. Створіть меню з 4 пунктами 1 - Додати учня 2 - Видалити учня за ім'ям 3 - Видалити учня за номером 4 - Вивести список учнів 0 - Виід. Якщо користувач ввів 1 запитайте у нього ім'я нового учня та додайте його до списку. Якщо коирстувач ввів 2 запитайте у нього ім'я учня та якщо такий є у списку видаліть його. Якщо користувач ввів 3 Запитайте у коирстувача номер учня перевірте що такий індекс існує та видаліть учня під цим індексом. Якщо коирстувач написав 4 виведіть саписок учнів з їх номерами. Якщо користувач написав 0 завершіть програму

students = []
while True:
    user_action = input("Enter your action: ")

    if user_action == '1':
        new_student_name = input("Enter name of a new student: ")
        students.append(new_student_name)
    elif user_action == '2':
        student_name = input("Enter name of the student to delete: ")
        if student_name in students:
            students.remove(student_name)
    elif user_action == '3':
        student_index = int(input("Enter student index: "))
        if 0 <= student_index < len(students):
            students.remove(student_index)
    elif user_action == '4':
        for i in range(len(students)):
            print(i, students[i])
    elif user_action == '0':
        print("Program finishes")
        break
    else:
        print('Enter valid instruction')



