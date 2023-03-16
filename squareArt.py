import numpy as np
import turtle

fill_chance = [0, 0, 20, 30, 20, 100, 101]
pattern1 = np.arange(4).reshape(2,2)
pattern2 = np.arange(9).reshape(3,3)

t = turtle.Turtle()
s = turtle.Screen()

def fill_square(width, x, y):
    t.fillcolor('black')
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(width)
        t.left(90)
    t.end_fill()
    t.penup()

def gen_square(width, level, x, y, maxL):
    if level < maxL:
        fill = np.random.randint(0, 99) < fill_chance[level]
        if fill:
            fill_square(width, x, y)

        else:
            shape = np.random.randint(1, 100) < 70
            if shape:
                for (i, j), _ in np.ndenumerate(pattern1):
                    width = width/2
                    gen_square(width, level + 1, x+i*width, y*j*width, maxL)
            else:
                for (i, j), _ in np.ndenumerate(pattern2):
                    width = width/3
                    gen_square(width, level + 1, x+i*width, y*j*width, maxL)

s.setup(600,600)
t.pencolor('red')
t.penup()
t.width(2)
t.goto(-200, -200)
gen_square(500, 0, -200, -200, 5)
turtle.done()