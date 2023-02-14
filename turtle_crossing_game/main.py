import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = []

screen.listen()
screen.onkeypress(key="w", fun=player.move)

level = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if random.randint(0, 101) < (30 + level*10):
        car_manager = CarManager()
        car_manager.speed_up(level)
        cars.append(car_manager)

    for car in cars:
        car.move()
        if car.xcor() < -330:
            cars.remove(car)
        elif player.distance(car.position()) <= 20.0:
            player.goto(0,0)
            player.write("Game over", align="center", font=("Courier", 24, "normal"))
            game_is_on = False

    if player.ycor() >= 280:
        player.level_up()
        level += 1
        scoreboard.clear()
        scoreboard.update_scoreboard()
        for car in cars:
            car.speed_up(level)
            time.sleep(0.01)



screen.exitonclick()
