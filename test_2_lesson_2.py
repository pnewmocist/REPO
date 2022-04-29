print("create your list")
n = int(input('enter numbers of members in your list:  '))
i = 0
my_list = []
while i <= n - 1:
    x = input(f"enter N{i}   ")
    my_list.append(x)
    print(my_list)
    i = i + 1
print("change number positions:1 to 2, 2 to 1")
x1 = int(input('enter number 1 to start:   '))
if x1 == 1:
    l = len(my_list)
    j = 0
    if l % 2 == 0:
        while j < l / 2:
            y = my_list.pop(1)
            my_list.append(y)
            z = my_list.pop(0)
            my_list.append(z)
            j = j + 1
    else:
        while j < l // 2:
            y = my_list.pop(1)
            my_list.append(y)
            z = my_list.pop(0)
            my_list.append(z)
            j = j + 1
            if j == l // 2:
                z = my_list.pop(0)
                my_list.append(z)
else:
    print("you don't start...")
print(my_list)
print('HAPPY END!!!')