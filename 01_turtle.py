"""
海龜繪圖 import turtle (不用透過pip安裝)
"""
import turtle as t

t.clear()


def function_drawcircle(Circle):
    t.penup()
    t.pensize = Circle.pensize
    t.goto(Circle.x, Circle.y)
    t.pendown()
    t.color(Circle.color)
    t.circle(Circle.r)


class Circle:
    def __init__(self, color, r, x, y, pensize):
        self.color = color
        self.r = r
        self.x = x
        self.y = y
        self.pensize = pensize

    def drawcircle(self):
        t.penup()
        t.pensize = self.pensize
        t.goto(self.x, self.y)
        t.pendown()
        t.color(self.color)
        t.circle(self.r)


c1 = Circle('red', 50, 0, 0, 5)
c2 = Circle('blue', 50, 100, 100, 5)

draw_type = input("1.function draw  2.class draw => ")
if draw_type == "1":
    function_drawcircle(c1)
    function_drawcircle(c2)
else:
    c1.drawcircle()
    c2.drawcircle()

any_key = input("press 【Enter key】 to continue.....")
