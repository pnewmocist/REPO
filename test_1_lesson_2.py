print('creat list and check it typing')
x = int(input('enter number 1 to start:   '))
if x == 1:
    list = [12, 34.5, 'true', 'gfds', True, False, 486]
    b = list
    i = 0
    l = len(b)
    while l > 0:
        print(type(b.pop(i)))
        l = len(b)
    print('happy end')
else:
    print("you don't start...")
