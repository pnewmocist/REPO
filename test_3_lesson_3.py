# Функция из трех аргументов суммирует два наибольших
def summ():
    arg_1 = float(input('enter argument_1:  '))
    arg_2 = float(input('enter argument_2:  '))
    arg_3 = float(input('enter argument_3:  '))
    x = [arg_1, arg_2, arg_3]
    s_full = sum(x) - min(x)
    return s_full

var_1 = summ()
print(var_1)
