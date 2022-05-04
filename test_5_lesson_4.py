k = 1  # По условию задачи нижняя граница - 100, верхняя граница - 1000
while k == 1:
    a = int(input("Введите нижнюю границу списка: "))
    b = int(input("Введите верхнюю границу списка: "))
    list_1 = [i for i in range(a, b + 1) if i % 2 == 0]
    print("Список четных чисел = ", list_1)
    import functools


    def my_func(prev_el, el):
        return prev_el * el


    c = functools.reduce(my_func, list_1)
    print("Произведение всех членов списка: = ", c)
    print("ИЛИ")
    list_2 = str(c)
    l = len(list_2)
    d = c / (10 ** (l - 1))
    print("Произведение всех членов списка: = ", f"{d:.3f} * 10^{l - 1}")
    print('если хотите повторить, введите 1, если нет - 0')
    k = int(input('1 / 0:  '))
print('end')
