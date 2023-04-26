from turtle import Turtle, Screen, colormode
from random import random, choice, randint

my_turtle = Turtle()
colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


def spirograph(size_gap):

    for i in range(int(360 / size_gap)):
        my_turtle.color(random_color())
        my_turtle.circle(100)
        current_heading = my_turtle.heading()
        my_turtle.setheading(current_heading + size_gap)


my_turtle.shape("turtle")
my_turtle.speed("fastest")

size = int(input("What size should you want to add for the Spirograph? "))
spirograph(size)


screen = Screen()
screen.exitonclick()
