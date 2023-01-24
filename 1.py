from turtle import *
import turtle

a = 1
p=1
z=1

print('Увеличить',
      'Уменьшить',
      'Выход',
      'Налево',
      'Направо',
      'Вверх',
      'Вниз')

x = input()
for i in x:
    if x == "Увеличить":
        a = 2
        turtle.setup(1000, 1000)
    elif x == "Уменьшить":
        a = 0.5
        turtle.setup(1000, 1000)
    if x == "Выход":
        quit()
    if x == "Направо":
        p = 150
    elif x == "Вверх":
        z = 150
    elif x == "Вниз":
        z = -150
    elif x == "Налево":
        p = - 150




class CurvesTurtle(Pen):
    def hilbert(self, size, level, parity):
        if level == 0:
            return
        self.left(parity * 90)
        self.hilbert(size, level - 1, -parity)
        self.forward(size)
        self.right(parity * 90)
        self.hilbert(size, level - 1, parity)
        self.forward(size)
        self.hilbert(size, level - 1, parity)
        self.right(parity * 90)
        self.forward(size)
        self.hilbert(size, level - 1, -parity)
        self.left(parity * 90)

    def fractal(self, dist, depth, dir):
        if depth < 1:
            self.fd(dist)
            return
        self.fractal(dist / 3, depth - 1, dir)
        self.lt(60 * dir)
        self.fractal(dist / 3, depth - 1, dir)
        self.rt(120 * dir)
        self.fractal(dist / 3, depth - 1, dir)
        self.lt(60 * dir)
        self.fractal(dist / 3, depth - 1, dir)


def main():
    ft = CurvesTurtle()
    ft.reset()
    ft.speed(-1000)
    ft.ht()
    ft.getscreen().tracer(1, 0)
    ft.pu()
    size = 6 * a
    ft.setpos(-33 * size + p, -32 * size + z)
    ft.pd()
    ft.fillcolor("red")
    ft.begin_fill()
    ft.fd(size)
    ft.hilbert(size, 6, 1)
    ft.fd(size)
    for i in range(3):
        ft.lt(90)
        ft.fd(size * (64 + i % 2))
    ft.pu()
    for i in range(2):
        ft.fd(size)
        ft.rt(90)
    ft.pd()
    for i in range(4):
        ft.fd(size * (66 + i % 2))
        ft.rt(90)
    ft.end_fill()


if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()
