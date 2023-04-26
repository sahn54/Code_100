from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape("turtle")
for turn in range(4):
    my_turtle.right(90)
    my_turtle.forward(100)


screen = Screen()
screen.exitonclick()
