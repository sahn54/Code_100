from turtle import Turtle
WIDTH = 5
HEIGHT = 1

STARTING_POSITIONS = [(350, 0), (-350, 0)]

# right paddle
# width = 20
# height = 100
# x_pos = 350
# y_pos = 0


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=WIDTH, stretch_len=HEIGHT)
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
