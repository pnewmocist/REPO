class Matrix:
    def __init__(self, n_1, n_2, n_3, n_4):
        self.n_1 = n_1
        self.n_2 = n_2
        self.n_3 = n_3
        self.n_4 = n_4

    def __str__(self):
        print(*(self.n_1), sep=' ')
        print(*(self.n_2), sep=' ')
        print(*(self.n_3), sep=' ')
        print(*(self.n_4), sep=' ')
        return f" "

    def __add__(self, other):
        c_1 = []
        c_2 = []
        c_3 = []
        c_4 = []
        if len(self.n_1) > len(other.n_1):
            other.n_1.extend([0, ] * (len(self.n_1) - len(other.n_1)))
            for i in range(len(self.n_1)):
                c_1.append((self.n_1[i] + other.n_1[i]))
        elif len(self.n_1) < len(other.n_1):
            self.n_1.extend([0, ] * (len(other.n_1) - len(self.n_1)))
            for i in range(len(other.n_1)):
                c_1.append((self.n_1[i] + other.n_1[i]))
        else:
            for i in range(len(self.n_1)):
                c_1.append((self.n_1[i] + other.n_1[i]))

        if len(self.n_2) > len(other.n_2):
            other.n_2.extend([0, ] * (len(self.n_2) - len(other.n_2)))
            for i in range(len(self.n_2)):
                c_2.append((self.n_2[i] + other.n_2[i]))
        elif len(self.n_2) < len(other.n_2):
            self.n_2.extend([0, ] * (len(other.n_2) - len(self.n_2)))
            for i in range(len(other.n_2)):
                c_2.append((self.n_2[i] + other.n_2[i]))
        else:
            for i in range(len(self.n_2)):
                c_2.append((self.n_2[i] + other.n_2[i]))

        if len(self.n_3) > len(other.n_3):
            other.n_3.extend([0, ] * (len(self.n_3) - len(other.n_3)))
            for i in range(len(self.n_3)):
                c_3.append((self.n_3[i] + other.n_3[i]))
        elif len(self.n_3) < len(other.n_3):
            self.n_3.extend([0, ] * (len(other.n_3) - len(self.n_3)))
            for i in range(len(other.n_3)):
                c_3.append((self.n_3[i] + other.n_3[i]))
        else:
            for i in range(len(self.n_3)):
                c_3.append((self.n_3[i] + other.n_3[i]))

        if len(self.n_4) > len(other.n_4):
            other.n_4.extend([0, ] * (len(self.n_4) - len(other.n_4)))
            for i in range(len(self.n_4)):
                c_4.append((self.n_4[i] + other.n_4[i]))
        elif len(self.n_4) < len(other.n_4):
            self.n_4.extend([0, ] * (len(other.n_4) - len(self.n_4)))
            for i in range(len(other.n_4)):
                c_4.append((self.n_4[i] + other.n_4[i]))
        else:
            for i in range(len(self.n_4)):
                c_4.append((self.n_4[i] + other.n_4[i]))

        return Matrix(c_1, c_2, c_3, c_4)


a_1 = Matrix([2, 3, 4], [5, 6, -9, 8], [9, 10, 7, 5], [13, 14, 16, 9, 8, 9])
print("Матрица_1")
print(a_1)

b_1 = Matrix([22, 33, 44, 8, 7], [55, 66, 77], [99, 88, 77, 66, 9], [55, 44, 33, 22, 9, 10])
print("Матрица_2")
print(b_1)

d_1 = Matrix([34, 52, 13, 24, 4], [65, 56, 87, 48, 4], [97, 83, 74, 4], [52, 41, 31, 20, 5, 6, 6])
print("Матрица_3")
print(d_1)

h_1 = Matrix([2, 12, 33, 3, 6], [15, 43, 106, 40, 6, 8], [47, 60, 7], [5, 4, 8])
print("Матрица_4")
print(h_1)

print("Матрица - Сумма")
print(a_1 + b_1 + d_1 + h_1)
