sizes = []
z = int(input("Хотите вводить данные? Если да, введите 1; если нет - введите 0: "))
if z == 1:
    v_1 = int(input("Введите количество клеток (4): "))
    for i in range(v_1):
        sizes.append(int(input(f"Введите количество ячеек {i + 1} клетки: ")))
   #print(sizes, type(sizes))
    print()

    arg = int(input("Введите количество аргументов в ряду: "))
    print()

    class Cells:
        def __init__(self, n_1):
            self.n_1 = n_1

        def __str__(self):
            return f"{self.n_1}"

        def make_order(self, rows):
            print('\n'.join(['$' * rows for _ in range(self.n_1 // rows)]))
            return '$' * (self.n_1 % rows)

        def __add__(self, other):
            c_1 = 0
            for i in range(len(sizes)):
                c_1 = ((self.n_1 + other.n_1))
            return Cells(c_1)

        def __sub__(self, other):
            c_2 = 0
            for i in range(len(sizes)):
                if self.n_1 >= other.n_1:
                    c_2 = ((self.n_1 - other.n_1))
                else:
                    c_2 = str("невозможно")
                    break
            return Cells(c_2)

        def __mul__(self, other):
            c_3 = 1
            for i in range(len(sizes)):
                c_3 = ((self.n_1 * other.n_1))
            return Cells(c_3)

        def __truediv__(self, other):
            c_4 = 0
            for i in range(len(sizes)):
                if self.n_1 >= other.n_1:
                    c_4 = round((self.n_1 / other.n_1), 0)
                else:
                    c_4 = str("невозможно")
                    break
            return Cells(c_4)

    a_1 = Cells(sizes[0])
    print(f"количество ячеек в первой клетке: {a_1.n_1}")
    print(a_1.make_order(arg))
    b_1 = Cells(sizes[1])
    print(f"количество ячеек во второй клетке: {b_1.n_1}")
    print(b_1.make_order(arg))
    d_1 = Cells(sizes[2])
    print(f"количество ячеек в третьей клетке: {d_1.n_1}")
    print(d_1.make_order(arg))
    l_1  = Cells(sizes[3])
    print(f"количество ячеек в четвертой клетке: {l_1.n_1}")
    print(l_1.make_order(arg))
    print(f"Сумма ячеек: {a_1 + b_1 + d_1 + l_1}")
    print(f"Вычитание: {l_1 - b_1}")
    print(f"Умножение: {b_1 * d_1}")
    print(f"Деление: {b_1 / l_1}")

else:
    print("end")
