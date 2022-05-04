from sys import argv # запуск скрипта

script_name, param_1, param_2 = argv

print("script name:  ", script_name)
print("Ввести целое число как нижнюю границу диапазона: ", param_1)
print("Ввести целое число как верхнюю границу диапазона:", param_2)

from itertools import count
for el in count(int(param_1)):
    if el > int(param_2):
        break
    print(el, end=', ')
