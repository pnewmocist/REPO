n = int(input('enter number:  '))
d = n
i = 0
y = 0
z = n * 10
while True:
    i = i + 1
    x = d % 10
    d = d // 10
    z = z % 10
    if x > z:
        if x > y:
            y = x
        else:
            y = y
    else:
        if z > y:
            y = z
        else:
            y = y
        if d == 0:
            break
print('max figure in your number: ', y, '   quantity figures in your number: ', i-1)
