import turtle as t
from turtle import Screen
import random

color_list = [(239, 234, 226), (220, 158, 84), (39, 109, 150), (120, 163, 191), (150, 63, 87), (217, 232, 222), (203, 134, 157), (180, 160, 34), (32, 131, 95), (122, 179, 152), (235, 218, 225), (161, 79, 52), (213, 87, 61), (197, 85, 112), (208, 223, 231), (229, 199, 114), (57, 166, 135), (141, 33, 42), (8, 104, 80), (47, 158, 182), (234, 163, 181), (117, 115, 162), (32, 62, 111), (236, 171, 157), (126, 38, 34), (156, 210, 197), (32, 57, 78), (70, 41, 37), (25, 65, 56), (74, 37, 47)]
painting = t.Turtle()
t.colormode(255)
painting.width(20)
painting.speed("fastest")


def random_color():
    color = random.choice(color_list)
    return color


def paint():
    painting.ht()
    painting.penup()
    y = -350
    for line in range(10):
        painting.setx(-225)
        y = y + 50
        painting.sety(y + 50)
        for dot in range(10):
            painting.color(random_color())
            painting.pendown()
            painting.shape("circle")
            painting.stamp()
            painting.penup()
            painting.forward(50)
            painting.pendown()
            painting.penup()


paint()

screen = Screen()
screen.exitonclick()
