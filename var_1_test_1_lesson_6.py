class TrafficLight:
    # атрибуты класса
    __color_1 = "Красный"
    color_2 = "Желтый"
    color_3 = "Зеленый"
    import time
    # методы класса
    def runnung(self):
        # print("\033[0m Горит ")
        print(f"\033[31m{self.__color_1}")
        TrafficLight.time.sleep(7)
        # print("\033[0m Горит ")
        print(f"\033[33m{self.color_2}")
        TrafficLight.time.sleep(3)
        # print("\033[0m Горит ")
        print(f"\033[32m{self.color_3}")
        TrafficLight.time.sleep(4)

    def runnung_1(self):
        print(f"\033[33m{self.color_2}")
        TrafficLight.time.sleep(1)


t = TrafficLight()
i = 1
while i <= 5:
    print("\033[0m")
    # print(f"Светофор горит {i}-й раз")
    t.runnung()
    i = i + 1
print("\033[0m")
# print("Светофор завис")
# print("Мигает")
t_1 = TrafficLight()
j = 1
while j <= 6:
    t_1.runnung_1()
    j = j + 1
print("\033[0m")
print("Погас")
