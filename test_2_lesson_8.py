while True:
    z = int(input("Если хотите работать с программой, введите 1; если нет - введите 0: "))

    class Division:
        def __init__(self, dl, dt):
            self.dl = dl
            self.dt = dt

        def __str__(self):
            return f'Делимое: {self.dl}\nДелитель: {self.dt}'

        def div(self, dl, dt):
            try:
                result = dl / dt
            except ZeroDivisionError:
                print("Деление на ноль недопустимо")
            else:
                print(f"Частное: {result:.2f}")

    if z == 1:
        dl = float(input("Введите делимое (любое рациональное число): "))
        dt = float(input("Введите делитель (любое рациональное число): "))
        ch = Division(dl, dt)
        print(ch)
        ch.div(dl, dt)
    else:
        print("Конец программы")
        break