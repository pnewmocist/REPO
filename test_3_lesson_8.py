list = []
while True:
    z = int(input("Если хотите работать с программой, введите 1; если хотите закончить - введите 0: "))


    class Number:

        def __init__(self, num):
            self.num = num

        def exception(self, num):
            list.append(num)
            print(list, type(list[0]))
            while True:
                z = int(input("Продолжить? Если да - введите 1, если нет - введите 0: "))
                if z == 1:
                    try:
                        num = float(input("Введите любое рациональное число: "))
                        list.append(num)
                        print(list, type(list[0]))
                    except ValueError:
                        print("Вы ввели не число!!!")
                        print(list, type(list[0]))
                else:
                    break


    if z == 1:
        try:
            num = float(input("Введите любое рациональное число: "))
            dt = Number(num)
            dt.exception(num)
        except ValueError:
            print("Вы ввели не число!")
            print(list, type(list[0]))
    else:
        print("Конец программы")
        break
