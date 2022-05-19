with open("text_1.txt", "a+", encoding='utf-8') as my_text_test_1:
    with open("text_1.txt", "r", encoding='utf-8') as my_text_test_1:
        l = my_text_test_1.readlines()
    len_test_1 = len(l)
    print(l, len_test_1)
z = int(input("Работаем с файлом?: введите 1, если да; введите 0, если нет: "))
if z == 1:
    t = int(input("Хотите вводить данные с нумерацией строк? Если да, введите 1; если нет - введите 0: "))
    with open("text_1.txt", "a+", encoding='utf-8') as my_text_test_1:
        c = len_test_1
        while True:
            if z == 1:
                c = c + 1
                str = input(f'Введите {c} строку: ')
                if t == 1:
                    print(f"{c} {str}", file=my_text_test_1)
                else:
                    print(f"{str}", file=my_text_test_1)
                z = int(input("Если нужна еще строка, введите 1, если нет, введите 0: "))
            else:
                my_text_test_1.seek(0)
                break
        for line in my_text_test_1:
            print(line, end='')
        print("end")
else:
    print("end")
