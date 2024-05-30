
# The Hirst Painting:
import turtle as t
from random import *

tt = t.Turtle()
tt.speed('fastest')
tt.hideturtle()

t.colormode(255)

def random_clr():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    tpl = (r, g, b)
    return tpl

tt.penup()
tt.goto(-200, -200)
tt.pendown()

for up in range(10):
    for move in range(10):
        tt.color(random_clr())
        tt.begin_fill()
        tt.circle(10)
        tt.end_fill()
        tt.penup()
        tt.forward(40)
        tt.pendown()
    y = tt.ycor()
    y += 40
    tt.penup()
    tt.goto(-200, y)
    tt.pendown()
    
t.done()