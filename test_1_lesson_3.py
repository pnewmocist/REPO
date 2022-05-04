# Дeление одного числа на второе - Вариант 1
a = float(input('введите числитель:  '))
b = float(input('введите знаменатель:  '))
if b == 0:
    print('деление на ноль выполнить невозможно')
elif b != 0:
    def func(a, b):
        return (a / b)


    print(f"{func(a, b):.4f}")

# Дeление одного числа на второе - Вариант 2
a = float(input('введите числитель:  '))
b = float(input('введите знаменатель:  '))
if b == 0:
    print('деление на ноль выполнить невозможно')
elif b != 0:
    def func():
        d = (a / b)
        return d


    result = func()
    print(f"{result:.3f}")


# Дeление одного числа на второе - Вариант 3
def func():
    try:
        x = float(input('введите числитель:  '))
        y = float(input('введите знаменатель:  '))
    except ValueError:
        return

    if y == 0:
        print('деление на ноль выполнить невозможно')
    elif y != 0:
        d = (x / y)
        return d


r = func()
print(r)
