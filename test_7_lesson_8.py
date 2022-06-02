class ComplexNumber:
    a = 0
    b = 0
    ad = 0
    sub = 0
    mult = 0
    div = 0
    def __init__(self, list_1):
        self.list_1 = list_1

    def addition(self):
        if (self.list_1[1] or self.list_1[3]) != 0:
            ComplexNumber.a = complex(self.list_1[0], self.list_1[1])
            print(f'Первое комплексоное число: {ComplexNumber.a}')
            ComplexNumber.b = complex(self.list_1[2], self.list_1[3])
            print(f'Второе комплексоное число: {ComplexNumber.b}')
            ComplexNumber.ad = ComplexNumber.a + ComplexNumber.b
            print(f'Сложение: {ComplexNumber.ad:.2f}')
            ComplexNumber.sub = ComplexNumber.a - ComplexNumber.b
            print(f'Вычитание: {ComplexNumber.sub:.2f}')
            ComplexNumber.mult = ComplexNumber.a * ComplexNumber.b
            print(f'Умножение: {ComplexNumber.mult:.2f}')
            ComplexNumber.div = ComplexNumber.a / ComplexNumber.b
            print(f'Деление: {ComplexNumber.div:.2f}')
        else:
            ComplexNumber.a = self.list_1[0]
            print(f'Первое целое число: {ComplexNumber.a}')
            ComplexNumber.b = self.list_1[2]
            print(f'Второе целое число: {ComplexNumber.b}')
            ComplexNumber.ad = ComplexNumber.a + ComplexNumber.b
            print(f'Сложение: {ComplexNumber.ad:.2f}')
            ComplexNumber.sub = ComplexNumber.a - ComplexNumber.b
            print(f'Вычитание: {ComplexNumber.sub:.2f}')
            ComplexNumber.mult = ComplexNumber.a * ComplexNumber.b
            print(f'Умножение: {ComplexNumber.mult:.2f}')
            ComplexNumber.div = ComplexNumber.a / ComplexNumber.b
            print(f'Деление: {ComplexNumber.div:.2f}')
        return f''

while True:
    list_1 = []
    for i in range(0, 3, 2):
        z_1 = float(input(f'Введите действительную часть {i // 2 + 1}-го комплексного числа: '))
        list_1.append(z_1)
        z_2 = float(input(f'Введите мнимую часть {i // 2+ 1}-го комплексного числа: '))
        list_1.append(z_2)
    itog = ComplexNumber(list_1)
    print()
    print(itog.addition())
    str = int(input("Повторить? Если да - введите 1, если нет - введите 0: "))
    if str == 1:
        continue
    else:
        print("КОНЕЦ ПРОГРАММЫ")
        break
