from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape("turtle")
for turn in range(50):
    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.forward(10)
    my_turtle.pendown()
screen = Screen()
screen.exitonclick()
