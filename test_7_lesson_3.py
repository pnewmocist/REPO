# Функция написания слов в предложении с прописной буквы
i = 1
while i == 1:
    def in_func():
        global y, z
        x = input('введите предложение латинскими буквами через пробел:  ')
        y = x.title()
        z = y.split('_')
        v = ' '.join(z)
        return v


    print(in_func())
    print(y)
    print(z)
    print('если хотите продолжить, введите 1, если нет - 0')
    i = int(input('1 / 0:  '))
print('end')
