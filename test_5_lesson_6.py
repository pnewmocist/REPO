class Stationery:
    title = "название /"
    color = "цвет /"
    square = "площадь зарисовки"

    def draw(self):
        print()
        print('Запуск отрисовки:')
        print(self.title, self.color, self.square)

st = Stationery()
st.draw()

class Pen(Stationery):
    title = "рисуем ручкой"
    color = "\033[34mсиним цветом\033[0m"
    square = "на одной страничке"
    def draw(self):
        print()
        print(self.title, self.color, self.square)
pd = Pen()
pd.draw()

class Pencil(Stationery):
    title = "малякаем карандашами"
    color = "\033[31mкрасным цветом\033[0m"
    square = "на двух страничках"
    def draw(self):
        print()
        print(self.title, self.color, self.square)
pnld = Pencil()
pnld.draw()

class Handle(Stationery):
    title = "малякаем маркерами"
    color = "\033[37mчерным цветом\033[0m"
    square = "и живого места не оставим"
    def draw(self):
        print()
        print(self.title, self.color, self.square)
hndld = Handle()
hndld.draw()



