from turtle import Turtle
MOVE_DISTANCE = 10

class Player_paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)
        self.setheading(90)
        self.color("white")
        self.penup()


    def l_paddle_up(self):
        self.fd(MOVE_DISTANCE)

    def l_paddle_down(self):
         self.bk(MOVE_DISTANCE)

    def r_paddle_up(self):
         self.fd(MOVE_DISTANCE)

    def r_paddle_down(self):
         self.bk(MOVE_DISTANCE)