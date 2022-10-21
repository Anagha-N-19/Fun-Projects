from turtle import Turtle, Screen, colormode
import random

c = ["purple", "red", "yellow", "green", "orange", "blue"]
s = Screen()
s.setup(width=500, height=400)
yv = [10, 40, 70, -20, -50, -80]
st = s.textinput("Welcome to race", "Whom do you bet on? (Colour)")
tlist = []
for i in range(0, 6):
    t = Turtle("turtle")
    t.color(c[i])
    t.penup()
    t.goto(-225, yv[i])
    tlist.append(t)
st = st.lower()
# print(st)
race = False
if st:
    race = True

while race:
    for i in tlist:
        if i.xcor() >= 190:
            race = False
            winner = i.color()
        r = random.randint(0, 10)
        i.forward(r)

if st == winner[0]:
    print("You win")
else:
    print(f"{winner[0]} is the winner. You lose")

s.exitonclick()
