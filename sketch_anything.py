from turtle import Turtle, Screen

t = Turtle()
s = Screen()
t.pensize(3)


def move_forward():
    t.forward(20)


def move_rt():
    t.right(10)


def move_left():
    t.left(10)


def move_back():
    t.backward(20)

def clearing():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

s.listen()

s.onkey(key="f", fun=move_forward)  # higher order function
s.onkey(key="l", fun=move_left)
s.onkey(key="r", fun=move_rt)
s.onkey(key="b", fun=move_back)
s.onkey(key="c",fun=clearing)
s.exitonclick()
