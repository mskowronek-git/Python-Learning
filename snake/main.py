from turtle import Screen, Turtle
import random
from body import Body

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

bodies = []

first_body = Turtle(shape = "square")
first_body.color("white")
first_body.penup()
first_body.shapesize(1, 1)

def create_body():


    if len(bodies) == 0:
        last_body = first_body
        # body_xpos = last_body.xcor()
        # body_ypos = last_body.ycor()
        body = Body(last_body.pos())
        body.setheading(last_body.heading())



    else:
        last_body = bodies[len(bodies) - 1]
    #     # body_xpos = last_body.x_cor()
    #     # body_ypos = last_body.y_scor()
        body = Body(last_body.position())
        body.setheading(last_body.heading())

    bodies.append(body)


food = Turtle(shape="circle")
food.color("white")
food.penup()
food.shapesize(0.7, 0.7)
food.speed("fastest")
food_xpos = random.randint(-290, 290)
food_ypos = random.randint(-290, 290)
food.setposition(food_xpos, food_ypos)

def food_gen():
    food_xpos = random.randint(-290, 290)
    food_ypos = random.randint(-290, 290)
    food.setposition(food_xpos, food_ypos)

play = True



def first_body_fd():
    first_body.fd(2)

    for body in bodies:
        body.movements.append(body.body_fd())

def first_body_left():
    first_body.left(90)

    for body in bodies:
        body.movements.append(body.body_left())

def first_body_right():
    first_body.right(90)

    for body in bodies:
        body.movements.append(body.body_right())


while play:

        if (first_body.distance(food.position())) < 15:
            food_gen()
            create_body()
            for i in range(9):
                first_body.fd(2)

        first_body_fd()

        screen.listen()
        what_heading = first_body.heading()
        if what_heading == 0.0:
            screen.onkey(key="a" and "d", fun=None)
            screen.onkey(key="w", fun=first_body_left)
            screen.onkey(key="s", fun=first_body_right)
        elif what_heading == 270.0:
            screen.onkey(key="w" and "s", fun=None)
            screen.onkey(key="d", fun=first_body_left)
            screen.onkey(key="a", fun=first_body_right)
        elif what_heading == 180.0:
            screen.onkey(key="a" and "d", fun=None)
            screen.onkey(key="s", fun=first_body_left)
            screen.onkey(key="w", fun=first_body_right)
        elif what_heading == 90.0:
            screen.onkey(key="w" and "s", fun=None)
            screen.onkey(key="a", fun=first_body_left)
            screen.onkey(key="d", fun=first_body_right)

        for body in bodies:
            body.setheading(first_body.heading())
            # first_element = body.movements[0]
            # print([bodies])
            # print(body.movements)
            # body.movements.remove(first_element)


screen.exitonclick()