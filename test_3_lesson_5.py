# Проверяем файл, с которым работаем на наличие информации
with open("text_4.txt", "r", encoding='utf-8') as my_text_test_3:
    len_test_3 = len(my_text_test_3.readlines())
    print("Исходное состояние файла: ")
    print(f"количество строк: {len_test_3}")
    print("Содержание: ")
    my_text_test_3.seek(0)
    for el in my_text_test_3:
        print(el, end='')
    print('')
    print('Конец списка')

with open("text_4.txt", "r", encoding='utf-8') as my_text_test_3:
    my_text_test_3.seek(0)  # Переводим курсор в начало текста
    len_list_1 = len(my_text_test_3.readlines()) # определяем количество строк в тексте
    my_text_test_3.seek(0) # Снова переводим курсор в начало текста
    list_2 = []
    list_3 = []
    for i in range(len_list_1):
        list_2 = my_text_test_3.readline() # Построчно выводим список фамилий с з/п
        list_3.append(tuple(list_2.split())) # формируем список и кортежей (фамилия - доход)
    #print(list_3, end='\n')
my_dict = {list_3[j][0]: float(list_3[j][1]) for j in range(0, len(list_3), 1)} # формируем словарь, где фамилия  это ключ, з/п - значение
#print(my_dict, end='\n')
sum_d = tuple(my_dict.values()) # Кортеж фамилий
name_d = tuple(my_dict.keys()) # Кортеж з/п
#print(name_d)
#print(sum_d)

import functools


def my_func(prev_el, el):
    return prev_el + el


c = (functools.reduce(my_func, sum_d) / len(list_3)) # определение среднего дохода из кортежа з/п
print(f"Средняя величина дохода сотрудников: {c:.2f} рублей")

list_4 = []
list_5 = []
for i in range(len(list_3)):
    if sum_d[i] < 20000:
        list_4.append(name_d[i])
        list_5.append(sum_d[i])
print("Сотрудники с доходом менее 20 000 рублей: ", list_4)
print(f'Их доход соответственно: {list_5} рублей')
