from sys import argv # запуск скрипта

script_name, param_1 = argv

print("script name:  ", script_name)
print("Ввести элементы списка без пробела: ", param_1)

from itertools import cycle
c = 0
l = len(param_1)
for el in cycle(param_1):
    if c > l * 7:
        break
    print(el, end=', ')
    c = c + 1