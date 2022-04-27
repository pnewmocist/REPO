# Функция возведения в степень Вар 1
def stepen(x, y):
    return x ** y

print(stepen(4, -5))


# Функция возведения в степень Вар 2
def stepen():
    x = float(input('введите действительное положительное число:  '))
    y = float(input('введите целое отрицательное число:  '))
    return x ** y


print(f"{stepen():.6f}")

# Функция возведения в степень Вар 3
def stepen():
    x = float(input('введите действительное положительное число:  '))
    y = float(input('введите целое отрицательное число:  '))
    z = abs(y)
    c = 1
    i = 1
    while i <= z:
        c = c * (1 / x)
        i = i + 1
    return(c)
d = stepen()
print(f"{d:.6f}")