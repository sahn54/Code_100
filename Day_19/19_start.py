from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()


def move_forward():
    my_turtle.forward(10)


screen.listen()
# space bar on the keyboard
screen.onkey(key="space", fun=move_forward)

screen.exitonclick()
