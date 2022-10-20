import random
from turtle import Turtle, Screen, colormode

# import colorgram
#rgbc = []
#print(rgbc)
# c = colorgram.extract('damienp.jpg', 30)
# for i in c:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     n = (r, g, b)
#     rgbc.append(n)

t = Turtle()
t.pensize(3)
colormode(255)
t.shape("turtle")
s = Screen()
t.setheading(225)
t.penup()
t.forward(280)
t.setheading(0)
l = [(233, 233, 232), (231, 233, 237), (236, 231, 233), (224, 233, 227), (207, 160, 82), (54, 88, 130), (145, 91, 40),
     (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143),
     (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92),
     (78, 153, 165),
     (194, 79, 73), (45, 74, 78), (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172),
     (219, 182, 169)]

for _ in range(10):
    for _ in range(10):
        t.dot(20, random.choice(l))
        t.penup()
        t.forward(50)
        t.pendown()
    t.penup()
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(500)
    t.right(180)
    t.pendown()
