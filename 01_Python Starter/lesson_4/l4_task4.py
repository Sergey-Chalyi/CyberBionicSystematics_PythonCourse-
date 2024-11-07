a = int(input("Enter a: "))
b = int(input("Enter b: "))

average = (a + b) / 2

for i in range(a, b + 1):
    if i % average == 0:
        print(i)