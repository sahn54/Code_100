from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()


def move_forward():
    my_turtle.forward(10)


def move_backwards():
    my_turtle.backward(10)


def turn_left():
    my_turtle.left(10)


def turn_right():
    my_turtle.right(10)


def clear_screen():
    # resetscreen better alternative!
    screen.resetscreen()
    # my_turtle.clear()
    # my_turtle.penup()
    # my_turtle.home()
    # my_turtle.pendown()


screen.listen()
# space bar on the keyboard
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()


# W = forwards
# S = backwards
# A = Counter-Clockwise
# D = Clockwise
# C = Clear Drawing
