# Завдання 2 

# Є два списки, які наповнюються користувачем з клавіатури. 
# Сформувати список, в якому будуть міститися унікальні значення 
# першого відносно другого списку та навпаки без повторень. 
# Роздрукувати підсумковий об'єкт на екран в прямій послідовності, 
# зворотній, а також виконати сортування за зростанням та спаданням.

num_list_1 = []
for _ in range(5):
    num_list_1.append(int(input("Enter num: ")))


num_list_2 = []
for _ in range(5):
    num_list_2.append(int(input("Enter num: ")))


final_list = []
for num in num_list_1:
    if num not in num_list_2:
        final_list.append(num)
for num in num_list_2:
    if num not in num_list_1:
        final_list.append(num)

print("direct final sequence:", final_list)
print("reverse final sequence:", final_list[::-1])
print("sort ascending:", sorted(final_list))
print("sort in descending order:", sorted(final_list, reverse=True))

