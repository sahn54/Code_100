from turtle import Turtle, Screen, colormode
from random import random, choice, randint

my_turtle = Turtle()
colormode(255)
angles = [0, 90, 180, 270]


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color


def randomWalk():
    random_angle = choice(angles)
    my_turtle.color(random_color())
    my_turtle.right(random_angle)
    my_turtle.forward(50)


my_turtle.shape("turtle")
my_turtle.speed("fast")
my_turtle.pensize(15)


for walk in range(50):
    randomWalk()


screen = Screen()
screen.exitonclick()
