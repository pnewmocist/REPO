while True:
    while True:
        try:
            print()
            z = int(input("Если хотите ввести дату, введите 1; если нет - введите 0: "))
            if z < 2:
                break
            else:
                print("Ввод неверен")
        except ValueError:
            print("Ввели не число")

    class Data:

        def __init__(self, text):
            self.text = text

        def __str__(self):
            return f'{self.text}'

        @classmethod
        def review(cls, text):
            i = 0
            list_1 = []
            text = text.split('-')
            while i < len(text):
                num = ''
                num_2 = 0
                for el in text[i]:
                    if el.isdigit() == True:
                        num = num + el
                        num_2 = int(num)
                list_1.append(num_2)
                i = i + 1
            print(list_1, type(list_1[0]))
            return Data.verify(list_1)

        @staticmethod
        def verify(list_1):
            if list_1[2] > 0:
                print("Летоисчисление нашей эры")
            else:
                print("Летоисчисление до нашей эры")
            if list_1[1] > 0 and list_1[1] < 13:
                print("Месяц введен верно")
                if list_1[0] <= 31 and (
                        list_1[1] == 1 or list_1[1] == 3 or list_1[1] == 5 or list_1[1] == 7 or list_1[1] == 8 or list_1[
                    1] == 10 or list_1[1] == 12):
                    print("Число введено верно")
                elif list_1[0] <= 30 and (list_1[1] == 4 or list_1[1] == 6 or list_1[1] == 9 or list_1[1] == 11):
                    print("Число введено верно")
                elif list_1[0] <= 28 and (list_1[1] == 2):
                    print("Число введено верно")
                elif list_1[0] == 29 and (list_1[1] == 2 and list_1[2] % 4 == 0):
                    print("Число введено верно. Високосный год.")
                else:
                    print("Число введено не корректно")
            else:
                print("Месяц введен не корректно. Число не может быть оценено.")


    if z == 1:
        while True:
            try:
                print()
                text = str(input("Введите число месяц год через тире (число - 2 цифры, месяц - 2 цифры, год - 4 цифры. Недостающие значения заполняются нулями): "))
                if len(text) == 10:
                    break
                else:
                    print("Ошибка ввода")
            except IndexError:
                print("Ошибка ввода")

        dt = Data(text)
        print(dt)
        Data.review(text)
    else:
        print("Конец программы")
        break