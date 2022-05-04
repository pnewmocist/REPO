k = 1
while k == 1:
    a = int(input("Введите количество членов Вашего списка: "))
    i = 0
    list_1 = []
    while i <= a - 1:
        b = int(input(f"Введите N{i}: "))
        list_1.append(b)
        i = i + 1
    print("list_1 = ", list_1)
    l = len(list_1)
    j = 0
    list_2 = [list_1[j] for j in range(0, l) if list_1.count(list_1[j]) == 1]
    print("list_2 = ", list_2)
    print('если хотите продолжить, введите 1, если нет - 0')
    k = int(input('1 / 0:  '))
print('end')
