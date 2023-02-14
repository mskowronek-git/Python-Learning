import turtle as t


class Body():

    def __init__(self, position):
        self.penup()
        self.shapesize(1, 1)
        self.speed("fastest")
        self.color("white")
        self.setposition(position)
        self.movements = []
        self.shape("square")

    def ontimer(self, fun, t):
        t.ontimer(fun, t)

    def setheading(self, angle):
        t.setheading(angle)

    def heading(self):
        t.heading()

    def position(self):
        t.pos()

    # def x_cor(self):
    #     t.xcor()
    #
    # def y_cor(self):
    #     t.ycor()

    def body_left(self):
        t.left(90)

    def body_right(self):
        t.right(90)

    def body_fd(self):
        t.fd(2)

    def penup(self):
        t.penup()

    def shapesize(self, param, param1):
        t.shapesize(param, param1)

    def speed(self, param):
        t.speed(param)

    def color(self, param):
        t.color(param)

    def setposition(self, position):
        t.setposition(position)

    def shape(self, param):
        t.shape(param)
