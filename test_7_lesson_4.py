import math

n = int(input("Введите целое положительное число: "))


def factorially():
    my_func = range(1, n + 1)
    for i in my_func:
        yield math.factorial(i)


fact = factorially()
j = 1
for el in fact:
    print(f"{j}! = {el}")
    j = j + 1
