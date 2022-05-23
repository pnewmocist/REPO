class Car:
    speed = 45
    color = "red"
    name = "LightCar"
    is_police = "notPolice"
    d = 0

    def __init__(self, c, n, i_p):
        self.color = c
        self.name = n
        self.is_police = i_p
        print()
        print(c, n, i_p)

    def go(self):
        print("The car \033[31m goes \033[0m")
    def stop(self):
        print("The car \033[31m stopes \033[0m")
    def turn_direction(self, d):
        if d == 0:
            print("The car turns \033[31m right \033[0m")
        elif d == 1:
            print("The car goes \033[31m ahead \033[0m")
        else:
            print("The car turns \033[31m left \033[0m")
    def show_speed(self, s):
        self.speed = s
        print(f"speed of car: \033[31m{self.speed} \033[0m km per hour")

class TownCar(Car):
    speed = 66
    color = "green"
    name = "\033[32m TownCar \033[0m"
    is_police = "notPolice"
    d = 0
    def show_speed(self, speed):
        if self.speed >= 60:
            print(f"speed of car: \033[31m{self.speed} \033[0m km per hour")
            print("\033[31m  Police! Police! \033[0m")
            print("speed of this car \033[31mexceeds!!! \033[0m")

tc = TownCar(TownCar.color, TownCar.name, TownCar.is_police)
tc.go()
tc.turn_direction(TownCar.d)
tc.show_speed(TownCar.speed)
print()

class SportCar(Car):
    speed = 75
    color = "yellow"
    name = "\033[33mSportCar\033[0m"
    is_police = "notPolice"
    d = 1
sc = SportCar(SportCar.color, SportCar.name, SportCar.is_police)
sc.go()
sc.turn_direction(SportCar.d)
sc.show_speed(SportCar.speed)

class WorkCar(Car):
    speed = 75
    color = "grey"
    name = "\033[37m WorkCar \033[0m"
    is_police = "notPlice"
    d = 2

    def show_speed(self, speed):
        if self.speed >= 60:
            print(f"speed of car: \033[31m{self.speed} \033[0m km per hour")
            print("\033[31m  Police! Police! \033[0m")
            print("speed of this car \033[31mexceeds!!! \033[0m")

wc = WorkCar(WorkCar.color, WorkCar.name, WorkCar.is_police)
wc.go()
wc.turn_direction(WorkCar.d)
wc.show_speed(WorkCar.speed)
print()

class PoliceCar(Car):
    speed = 60
    color = "blue"
    name = "\033[34m LightCar \033[0m"
    is_police = "Police"
pc = PoliceCar(PoliceCar.color, PoliceCar.name, PoliceCar.is_police)
pc.stop()

























