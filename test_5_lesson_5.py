# Проверяем файл, с которым работаем на наличие информации
with open("text_7.txt", "r", encoding='utf-8') as my_text_test_7:
    len_test_7 = len(my_text_test_7.readlines())
    print("Исходное состояние файла: ")
    print(f"количество строк: {len_test_7}")
    print("Содержание: ")
    my_text_test_7.seek(0)
    for el in my_text_test_7:
        print(el, end='')
    print('')
    print('Конец списка')


z = int(input("Хотите вводить данные? Если да, введите 1; если нет - введите 0: "))
if z == 1:
    with open("text_7.txt", "a+", encoding='utf-8') as my_text_test_7:
        len_test = len(my_text_test_7.readlines())
        c = len_test
        while True:
            if z == 1:
                c = c + 1
                str = float(input(f'Введите {c} число: '))
                print(f"{str}", file=my_text_test_7, end=' ')
                z = int(input("Если нужно еще число, введите 1, если нет, введите 0: "))
            else:
                my_text_test_7.seek(0)
                break
        for line in my_text_test_7:
            print(line, end='')
        print(" ")

        with open("text_7.txt", "r", encoding='utf-8') as my_text_test_7:
            list_1 = my_text_test_7.readline()
            list_2 = list_1.split()
            len_1 = len(list_2)
            list_3 = []
            for i in range(len_1):
                list_3.append(float(list_2[i]))
            #print(list_3)

        import functools


        def my_func(prev_el, el):
            return prev_el + el


        c = (functools.reduce(my_func, list_3))  # определение суммы
        print(f"Сумма чисел в строке: {c:.2f}")
        print('Конец программы')
else:
    print("end")
