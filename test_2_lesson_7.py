from abc import ABC, abstractmethod

size = 47 # Для пальто
number = 14
hight = 1.76 # Для костюма
quantity = 18


class Clothes(ABC):
    c_1 = 0

    def __init__(self, n_1):
        self.n_1 = n_1

    def __add__(self, other):
        Clothes.c_1 = self.calc + other.calc
        return Clothes.c_1


class Coat(Clothes):

    @property
    def calc(self):
        print(f"Пошло ткани на одно пальто: {(round(((self.n_1) / 6.5 + 0.5), 1))} метров на размер {self.n_1}")
        print(f"Расход ткани на пошив {number} пальто: {(((((self.n_1) / 6.5 + 0.5))) * number):.1f} метров")
        return (round(((self.n_1) / 6.5 + 0.5), 1)) * number


class Costume(Clothes):

    @property
    def calc(self):
        print(f"Пошло ткани на один костюм: {round(((self.n_1) * 2 + 0.3), 1)} метров на рост {(self.n_1) * 100} сантиметров")
        print(f"Расход ткани на пошив {quantity} костюмов: {(((self.n_1) * 2 + 0.3) * quantity):.1f} метров")
        return (round(((self.n_1) * 2 + 0.3), 1)) * quantity


a_1 = Coat(size)
b_1 = Costume(hight)
print()
print(f"Расход ткани на пошив пальто и костюма: {(a_1 + b_1):.1f} метров")
