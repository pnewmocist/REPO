# Функция сложения введенных чисел
i = 1
c = 0
while i == 1:
    def int_func():
        global i, c
        a = input('введите строку чисел через пробел:  ')
        b = a.split(' ')
        l = len(b)
        while i <= l:
            d = b.pop(0)
            try:
                e = float(d)
            except ValueError:
                return c, None
            c = c + e
            i = i + 1
        return c

    v_summ = int_func()
    print(f"Сумма введенных чисел: {v_summ}")
    print('если хотите продолжить, введите 1, если нет - 0')
    i = input('1 / 0:  ')
    if i == "1 ":
        i = int(i)
    elif i == "0":
        print("Всё!")
    else:
        print('Ошибка')
print('Конец!')
