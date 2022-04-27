n = int(input('insert any positive number:  '))
i = 0
d = n
while True:
    d = d // 10
    i = i + 1
    if d < 0.1:
        break
k = i
print('quantity of figures in number =',k)
n1 = n
n2 = n * (10 ** (k)) + n1
n3 = n * (10 ** (2 * k)) + n * (10 ** (k)) + n1
print('summ n+nn+nnn =  ', n1 + n2 + n3)
