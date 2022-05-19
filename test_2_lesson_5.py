with open("text_3.txt", "r", encoding='utf-8') as my_text_test_2:
    len_test_2 = len(my_text_test_2.readlines())
    print("Исходное состояние файла: ")
    print(f"количество строк: {len_test_2}")
    print("Содержание: ")
    my_text_test_2.seek(0)
    for el in my_text_test_2:
        print(el, end='')
    print('')

v = 0
z = int(input("Работаем с файлом?: введите 1, если да; введите 0, если нет: "))
if z == 1:
    with open("text_3.txt", "a+", encoding='utf-8') as my_text_test_2:
        c = len_test_2
        while True:
            v = int(input("Если нужна еще строка, введите 1, если нет, введите 0: "))
            if v == 1:
                str = input('Вводите: ')
                print(f"{str}", file=my_text_test_2)
            else:
                break
    with open("text_3.txt", "r", encoding='utf-8') as my_text_test_2:
        k = 0
        print("ВВЕДЕННЫЙ ТЕКСТ:")
        for el in my_text_test_2:
            k = k + 1
            print(f"строка {k}: ", el, end='')
            l_2 = len(el.split(' '))
            print(f"Количество слов в {k} строке: {l_2}")
        my_text_test_2.seek(0)
        l = my_text_test_2.readlines()
        len_test_2 = len(l)
        print("Количество строк: ", len_test_2)
print('Конец программы')
