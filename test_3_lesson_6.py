class Worker:
    # атрибуты класса
    name = "Дионисий"
    surname = "Пластилинофф"
    position = "менеджер улиц"
    __income = {"оклад": 7000, "премия": 4000}
    income_1 = __income
    #print(income_1)

class Position(Worker):
    def get_full_name(self):
        print()
        print(f"Получаю целое имя: {self.name} {self.surname}")
    def get_total_income(self):
        print(f"Зарплата: {self.income_1.get('оклад') + self.income_1.get('премия')} рублей")

w_1 = Position()
z = int(input("Хотите ввести данные другого человека? Если да, введите 1, если нет - 0: "))
if z == 1:
    w_1.name = input("Введите имя: ")
    w_1.surname = input("Введите фамилию: ")
    w = int(input("Введите оклад: "))
    b = int(input("Введите премию: "))
    new_income = {"оклад": w, "премия": b}
    w_1.income_1.update(new_income)
    #print(w_0.income)
print()
print(f"Проверяю атрибуты: Имя: {w_1.name}, Фамилия: {w_1.surname}, Оклад: {w_1.income_1.get('оклад')} рублей, Премия: {w_1.income_1.get('премия')} рублей")
w_1.get_full_name()
w_2 = Position()
w_2.get_total_income()



