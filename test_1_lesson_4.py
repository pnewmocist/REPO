from sys import argv # запуск скрипта

script_name, param_1, param_2, param_3, param_4, param_5, param_6 = argv

print("script name:  ", script_name)
print("Расчет зарплаты работнику, Фамилия: ", param_1)
print("                           Имя: ", param_2)
print("                           Отчество: ", param_3)
print("выработка в часах:  ", param_4, "часов")
print("ставка в час:  ", param_5, "рублей")
print("премия:  ", param_6, "рублей")
print("Зарплата: ", (int(param_4) * int(param_5))+int(param_6), "рублей")
