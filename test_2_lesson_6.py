class Road:
    # атрибуты класса
    __length = "length"
    __width = "width"
    # методы класса
    def asphalt_mass(self, __length, __width):
        print()
        print(f"Масса асфальта для покрытия дороги длиной \033[31m{__length} \033[0m метров "
              f"и шириной \033[31m{__width} \033[0m метров: \033[31m{__length * __width * 25 * 5} \033[0m кг "
              f"или \033[31m{__length * __width * 25 * 5 / 1000} \033[0m тонн")

r = Road()
r.asphalt_mass(60,5000)