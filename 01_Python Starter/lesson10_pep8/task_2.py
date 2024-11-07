import math, random
from math import pi
from math import e


PRINT = 5

count = int(input(' Введите количество повторов : '))

print(PRINT*count )
print(pi*PRINT*count)
print (e*2)

while PRINT >= 0:
    PRINT-=1

my_str = 'my string'
my_sum = 0

for elem in my_str:
    my_sum += pow(my_str.find(elem), 2)
    print("sum=", sum)


def my_func(atr = 1):
    print(' atr', atr)

print(my_func(atr = 5))