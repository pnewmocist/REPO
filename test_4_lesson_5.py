# Проверяем файл, с которым работаем на наличие информации
with open("text_5.txt", "r", encoding='utf-8') as my_text_test_4:
    len_test_4 = len(my_text_test_4.readlines())
    print("Исходное состояние файла: ")
    print(f"количество строк: {len_test_4}")
    print("Содержание: ")
    my_text_test_4.seek(0)
    for el in my_text_test_4:
        print(el, end='')
    print('')
    print('Конец списка')

with open("text_5.txt", "r", encoding='utf-8') as my_text_test_4:
    my_text_test_4.seek(0)  # Переводим курсор в начало текста
    len_list_1 = len(my_text_test_4.readlines()) # определяем количество строк в тексте
    my_text_test_4.seek(0) # Снова переводим курсор в начало текста
    list_2 = []
    list_3 = []
    for i in range(len_list_1):
        list_2 = my_text_test_4.readline() # Построчно выводим список фамилий с з/п
        list_3.append(tuple(list_2.split('-'))) # формируем список и кортежей (фамилия - доход)
    #print(list_3, end='\n')
my_dict = {list_3[j][0]: (list_3[j][1]) for j in range(0, len(list_3), 1)} # формируем словарь, где фамилия  это ключ, з/п - значение
#print(my_dict, end='\n')
sum_d = tuple(my_dict.values()) # Кортеж фамилий
name_d = tuple(my_dict.keys()) # Кортеж з/п
#print(name_d)
#print(sum_d)

with open("text_6.txt", "a+", encoding='utf-8') as my_text_test_5:
    str = []
    for i in range(len(list_3)):
        print(name_d[i])
        str = input(f'Введите перевод в {i + 1} строку: ')
        print(f"{str} -{sum_d[i]}", end='', file=my_text_test_5)

with open("text_6.txt", "r", encoding='utf-8') as my_text_test_6:
    my_text_test_6.seek(0)
    for el in my_text_test_6:
        print(el, end='')
    print('')
    print('Конец списка')