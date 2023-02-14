from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1,2)
        self.setposition(300, random.randint(-260, 260))
        self.setheading(180)
        self.color(random.choice(COLORS))
        self.move_speed = STARTING_MOVE_DISTANCE

    def move(self):
        self.fd(self.move_speed)

    def speed_up(self, level):
        self.move_speed += MOVE_INCREMENT * level

