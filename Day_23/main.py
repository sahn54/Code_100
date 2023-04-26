import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

the_player = Player()
cars = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(the_player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()


# detect collision with car
    for car in cars.all_cars:
        if car.distance(the_player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # if the_player.distance(cars) < 50:
    #     scoreboard.game_over()


# if the the player reaches to the final line
    if the_player.is_at_finish_line():
        the_player.go_to_start()
        cars.level_up()
        scoreboard.increase_score()

screen.exitonclick()
