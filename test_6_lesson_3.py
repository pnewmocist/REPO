# Функция написания слов с прописной буквы
i = 1
while i == 1:
    def int_func():
        x = input('введите слово латинскими буквами:  ')
        z = x.title()
        return z


    print(int_func())
    print('если хотите продолжить, введите 1, если нет - 0')
    i = int(input('1 / 0:  '))
print('end')


