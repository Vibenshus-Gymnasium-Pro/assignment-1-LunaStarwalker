import turtle
import random
import math

density = 20
size = 500
len = 30
angle = 360/density

turt = turtle.Turtle()
screen = turtle.Screen()

screen.setup(size, size)

turt.penup()
turt.goto(0, 0)
turt.fillcolor('#FF0000')

def draw_line(row):
    turt.pendown()
    turt.forward(row*10)
    turt.right(540/8)
    turt.penup()


for row in range(density):
    for i in range(5):
        draw_line(row)

turt.end_fill()

