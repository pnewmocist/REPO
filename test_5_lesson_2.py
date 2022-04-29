a = int(input('enter some figure more than 0:  '))
b = [7, 5, 5, 3, 2, 1]
i = 0
j = 0
l = len(b)
print(b)
while i < l:
    if a > b[i]:
        b.insert(i, a)
        break
    else:
        i = i + 1
if i == l:
    b.append(a)
c = b
print(c)

