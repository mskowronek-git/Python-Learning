from turtle import Turtle, Screen
from player_paddle import Player_paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Player_paddle((350, 0))
l_paddle = Player_paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="w", fun=l_paddle.l_paddle_up)
screen.onkeypress(key="s", fun=l_paddle.l_paddle_down)
screen.onkeypress(key="Up", fun=r_paddle.r_paddle_up)
screen.onkeypress(key="Down", fun=r_paddle.r_paddle_down)

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.bound_out()
        scoreboard.l_point()
        scoreboard.update_scoreboard()

    if ball.xcor() < -380:
        ball.bound_out()
        scoreboard.r_point()
        scoreboard.update_scoreboard()

screen.exitonclick()
