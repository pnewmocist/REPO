a = int(input("enter number of month as a figure: "))
b = {12:'winter',1:'winter',2:'winter',3:'spring',4:'spring',5:'spring',6:'summer',7:'summer',8:'summer',9:'autunm',10:'autunm',11:'autunm'}
c = b.setdefault(a)
print(c)

