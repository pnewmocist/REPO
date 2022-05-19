# Проверяем файл, с которым работаем на наличие информации
with open("text_9.txt", "r", encoding='utf-8') as my_text_test_9:
    list_1 = my_text_test_9.readlines()
    len_test_9 = len(list_1)
    print("Исходное состояние файла: ")

    print("Содержание: ")
    my_text_test_9.seek(0)
    for el in my_text_test_9:
        print(el, end='')
    print('')
    print(f"количество строк: {len_test_9}")
lenst = []
with open("text_9.txt", "r", encoding='utf-8') as my_text_test_9:
    for i in range(len_test_9):
        list_1 = list((my_text_test_9.readline()).split())
        len_2 = len(list_1)
        lenst.append(len_2)
    # print(lenst)
    print(f"Количество знаков в строках: {lenst}")
print('Конец списка')

with open("text_9.txt", "r", encoding='utf-8') as my_text_test_9:
    list_1 = my_text_test_9.readlines()
    len_1 = len(list_1)  # Количество строк
    # print(list_1, len_1)
    # print(list_1[0])

j = 0
list_4 = []
while j < len_1:
    list_2 = list_1[j].split() # Выделяем первую строку и разбиваем ее на слова
    len_2 = len(list_2) # Определяем количество слов в первой строке
    # print(list_2, len_2)

    i = 0
    list_3 = []
    # print(list_2[i])
    while i < len_2: # Выделяем слово в выбранной строке
        num = ''
        num_2 = 0
        for el in list_2[i]:
            if el.isdigit() == True: # Определяем наличие цифр в слове
                num = num + el
                num_2 = (int(num)) * (-1) ** (i) # перевод в целочисленное значение
        # print(num_2, type(num_2))
        list_3.append(num_2) # формирование списка из чисел анализируемой строки
        i = i + 1
    # print(list_3)
    sum_1 = sum(list_3)  # арифметическое действие по условию задачи
    # print(sum_1)
    list_4.append(sum_1) # формирование списка значений по результатам анализа всех строк
    j = j + 1
    # print(f"Прибыль: {list_4}")
    # print(list_4[0])

per = 0
print(f"Прибыль: {list_4}")
list_7 = [el for el in list_4 if el > 0]
per = round((sum(list_7)) / len(list_7), 2)
average_profit = (per)
print(f"Только прибыль: {list_7}, средняя прибыль: {average_profit:.2f}")

with open("text_9.txt", "r", encoding='utf-8') as my_text_test_9:
    my_text_test_9.seek(0)  # Переводим курсор в начало текста
    len_list_1 = len(my_text_test_9.readlines())  # определяем количество строк в тексте
    my_text_test_9.seek(0)  # Снова переводим курсор в начало текста
    list_5 = []
    list_6 = []
    for i in range(len_list_1):
        list_5 = my_text_test_9.readline()  # Построчно выводим список
        list_6.append(list(list_5.split()))  # формируем список и кортежей (фамилия - доход)
    # print(list_6, end='\n')
my_dict = {list_6[k][0]: list_6[k][1:lenst[k - 1]] for k in
           range(0, len(list_6), 1)}  # формируем словарь, где фамилия  это ключ, з/п - значение
# print(my_dict, end='\n')
sum_d = list(my_dict.values())  # Кортеж фамилий
name_d = list(my_dict.keys())  # Кортеж з/п
# print(name_d)

my_dict_2 = {name_d[n]: list_4[n] for n in range(0, len_1)}
print(f"Итоговый словарь фирм: {my_dict_2}")
my_dict_3 = {'average_profit': per}
print(f"Словарь средней прибыли: {my_dict_3}")
list_8 = [my_dict_2, my_dict_3]
print("Итоговый список:", list_8)

import json
data = [my_dict_2, my_dict_3]
with open ('my_file.json.py', 'w') as write_f:
    json.dump(data, write_f)
