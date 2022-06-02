class Store:
    pr = 0
    px = 0
    mass = {}
    new_dict = {}
    def __init__(self, z_1, z_2, data):
        self.z_1 = z_1
        self.z_2 = z_2
        self.data = data

    def addition(self):
        if self.z_2 != 0:
            Store.pr = list(self.data.keys())[self.z_1 - 1]
            Store.px = self.data.get(list(self.data.keys())[self.z_1 - 1])
            Store.px = Store.px + self.z_2
            Store.new_dict = {Store.pr: Store.px}
            self.data.update(Store.new_dict)
            Store.mass = self.data
            if self.z_2 > 0:
                print(f"После добавления {self.z_2} экземпляров модели {Store.pr} стало {Store.mass}")
            elif self.z_2 < 0:
                print(f"После передачи {(self.z_2) * (-1)} экземпляров модели {Store.pr} осталось {Store.mass}")
        else:
            print(f"Ничего не добавлено и не передано: {self.data}")

    def __str__(self):
        return f''


class OrgTechnics:

    def __init__(self, data_1):
        self.data_1 = data_1

    def __str__(self):
        return f' {self.data_1}'

    def summa(self, data_1):
        sums = 0
        for el in list(self.data_1.values()):
            sums = sums + el
        return sums


class Printer(OrgTechnics):
    def __str__(self):
        return f'Имеющиеся на складе принтеры: {OrgTechnics(data_2)}'

class Scaner(OrgTechnics):
    def __str__(self):
        return f'Имеющиеся на складе сканеры: {OrgTechnics(data_3)}'

class Xerox(OrgTechnics):
    def __str__(self):
        return f'Имеющиеся на складе ксероксы: {OrgTechnics(data_4)}'

mass_2 = {}
mass_3 = {}
mass_4 = {}
spisok = ['printer', 'scaner', 'xerox']

while True:
    data_2 = {'HP': 5, 'Pentium': 3, 'Canon': 7}
    data_2.update(mass_2)
    data_3 = {'Fujitsu': 15, 'Brother': 0, 'Epson': 3}
    data_3.update(mass_3)
    data_4 = {'Bizhub': 9, 'Color': 6, 'LaserJet': 4}
    data_4.update(mass_4)
    data_1 = {'printer': sum(list(data_2.values())), 'scaner': sum(list(data_3.values())),'xerox': sum(list(data_4.values()))}

    while True:
        try:
            print()
            z = int(input("Чтобы просмотреть содержимое склада введите 1; чтобы просмотреть содержимое оргтехники - введите 2;\nчтобы добавить оргтехнику на склад или передать куда-либо - введите 3; чтобы выйти - введите 0:  "))
            if z < 4:
                break
            else:
                print("Ввод неверен")
        except ValueError:
            print("Ввели не число")

    if z == 1:
        cop_1 = OrgTechnics(data_1)
        print()
        print(f'Содержимое склада: {cop_1}')
        print('Всего единиц: ', end='')
        print(cop_1.summa(data_1))

    elif z == 3:
        while True:
            while True:
                print()
                str = input('Введите название техники, которую хотите добавить или передать (printer, scaner, xerox); чтобы выйти введите 0:  ')
                if str == spisok[0]:
                    break
                elif str == spisok[1]:
                    break
                elif str == spisok[2]:
                    break
                elif str == '0':
                    break
                else:
                    print("Ввод неверен")

            if str == 'printer':
                cop_2 = Printer(data_2)
                print(cop_2)
                print()
                z_0 = int(input('Если вам нужно передать оргтехнику кудо-либо - введите 1, если нужно добавить на склад - введите 2: '))
                if z_0 == 2:
                    print()
                    z_1 = int(input('Чтобы добавить количество изделий введите цифру, соответствующую модели в списке (1, 2 или 3): '))
                    z_2 = int(input('Введите количество добавляемого изделия: '))
                elif z_0 == 1:
                    print()
                    z_1 = int(input('Выберите модель для передачи - введите цифру, соответствующую модели в списке (1, 2 или 3): '))
                    z_2 = (int(input('Введите количество передаваемого изделия: ')) * (-1))
                cop_5 = Store(z_1, z_2, data_2)
                print(cop_5)
                cop_5.addition()
                mass_2 = Store.mass
                print()
                v_1 = int(input('Чтобы продолжить добавление/передачу- введите 1; чтобы выйти - введите 0: '))
                if v_1 == 0:
                    break
                if v_1 == 1:
                    continue
            if str == 'scaner':
                cop_3 = Scaner(data_3)
                print(cop_3)
                print()
                z_0 = int(input('Если вам нужно передать оргтехнику кудо-либо - введите 1, если нужно добавить на склад - введите 2: '))
                if z_0 == 2:
                    print()
                    z_1 = int(input('Чтобы добавить количество изделий введите цифру, соответствующую модели в списке (1, 2 или 3): '))
                    z_2 = int(input('Введите количество добавляемого изделия: '))
                elif z_0 == 1:
                    print()
                    z_1 = int(input('Выберите модель для передачи - введите цифру, соответствующую модели в списке (1, 2 или 3): '))
                    z_2 = (int(input('Введите количество передаваемого изделия: ')) * (-1))
                cop_6 = Store(z_1, z_2, data_3)
                print(cop_6)
                cop_6.addition()
                mass_3 = Store.mass
                print()
                v_1 = int(input('Чтобы продолжить добавление/передачу - введите 1; чтобы выйти - введите 0:  '))
                if v_1 == 0:
                    break
                if v_1 == 1:
                    continue
            if str == 'xerox':
                cop_4 = Xerox(data_4)
                print(cop_4)
                print()
                z_0 = int(input('Если вам нужно передать оргтехнику кудо-либо - введите 1, если нужно добавить на склад - введите 2: '))
                if z_0 == 2:
                    print()
                    z_1 = int(input('Чтобы добавить количество изделий введите цифру, соответствующую модели в списке (1, 2 или 3): '))
                    z_2 = int(input('Введите количество добавляемого изделия: '))
                elif z_0 == 1:
                    print()
                    z_1 = int(input('Выберите модель для передачи - введите цифру, соответствующую модели в списке (1, 2 или 3): '))
                    z_2 = (int(input('Введите количество передаваемого изделия: ')) * (-1))
                cop_7 = Store(z_1, z_2, data_4)
                print(cop_7)
                cop_7.addition()
                mass_4 = Store.mass
                print()
                v_1 = int(input('Чтобы продолжить добавление - введите 1; чтобы выйти - введите 0:  '))
                if v_1 == 0:
                    break
                if v_1 == 1:
                    continue
            else:
                break

    elif z == 2:
        while True:
            while True:
                print()
                v = input('Чтобы просмотреть сoдержимое техники - введите ее название (printer, scaner, xerox); чтобы выйти введите 0:  ')
                if v == spisok[0]:
                    break
                elif v == spisok[1]:
                    break
                elif v == spisok[2]:
                    break
                elif v == '0':
                    break
                else:
                    print("Ввод неверен")

            if v == 'printer':
                cop_2 = Printer(data_2)
                print(cop_2)
                print('Всего единиц: ', end='')
                print(cop_2.summa(data_2))
                print()
                v_1 = int(input('Чтобы продолжить просмотр содержания техники - введите 1; чтобы выйти - введите 0:  '))
                if v_1 == 0:
                    break
                if v_1 == 1:
                    continue
            if v == 'scaner':
                cop_3 = Scaner(data_3)
                print(cop_3)
                print('Всего единиц: ', end='')
                print(cop_3.summa(data_3))
                print()
                v_1 = int(input('Чтобы продолжить просмотр содержания техники - введите 1; чтобы выйти - введите 0:  '))
                if v_1 == 0:
                    break
                if v_1 == 1:
                    continue
            if v == 'xerox':
                cop_4 = Xerox(data_4)
                print(cop_4)
                print('Всего единиц: ', end='')
                print(cop_4.summa(data_4))
                print()
                v_1 = int(input('Чтобы продолжить просмотр содержания техники - введите 1; чтобы выйти - введите 0:  '))
                if v_1 == 0:
                    break
                if v_1 == 1:
                    continue
            else:
                break

    else:
        print()
        print("КОНЕЦ ПРОГРАММЫ")
        break