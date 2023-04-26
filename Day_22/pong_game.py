from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)


paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
pong_ball = Ball()
our_scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")

game_is_on = True
while game_is_on:

    time.sleep(pong_ball.move_speed)
    screen.update()
    pong_ball.move()

    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce_y()

    # Detect collision with paddle_right or paddle_left
    if pong_ball.distance(paddle_right) < 50 and pong_ball.xcor() > 320 or pong_ball.distance(paddle_left) < 50 and pong_ball.xcor() < -320:
        pong_ball.bounce_x()
    # Detect if the ball goes out of bound at the edge of the screen
    if pong_ball.xcor() > 380:
        pong_ball.reset_ball()
        our_scoreboard.l_point()  # type: ignore

    if pong_ball.xcor() < -380:
        pong_ball.reset_ball()
        our_scoreboard.r_point()  # type: ignore


screen.exitonclick()
