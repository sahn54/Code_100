from turtle import Turtle, Screen
from random import random


def solution(num_side):
    my_turtle.color(random(), random(), random())
    angle = 360 / num_side
    for i in range(num_side):

        my_turtle.right(angle)
        my_turtle.forward(100)


my_turtle = Turtle()
my_turtle.shape("turtle")

for side in range(3, 11):
    solution(side)


screen = Screen()
screen.exitonclick()
