k = 1
while k == 1:
    a = int(input("Введите количество членов Вашего списка: "))
    j = 0
    list_1 = []
    while j <= a - 1:
        b = int(input(f"Введите N{j}: "))
        list_1.append(b)
        j = j + 1
    print(list_1)
    l = len(list_1)
    list_2 = [list_1[i] for i in range(0, l) if list_1[i] > list_1[i - 1]]
    print(list_2)
    print('если хотите продолжить, введите 1, если нет - 0')
    k = int(input('1 / 0:  '))
print('end')