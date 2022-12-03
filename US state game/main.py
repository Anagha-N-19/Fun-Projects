import turtle
import pandas as pd

s = turtle.Screen()
s.title("US State Game")
image = "blank_states_img.gif"
s.addshape(image)
turtle.shape(image)

# def get_mouse_click_coord(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coord)
#
data = pd.read_csv("50_states.csv")
datalist = data['state'].to_list()
guess = []

while(len(guess)<50):
    answer = s.textinput(title=f"{len(guess)}/50 states", prompt="State name :")
    answer = answer.title()
    if answer == "Exit":
        notlist = []
        for i in datalist:
            if i not in guess:
                notlist.append(i)
        new_data = pd.DataFrame(notlist)
        new_data.to_csv("Missing states.csv")
        break
    if answer in datalist:
        guess.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_info = data[data.state == answer]
        t.goto(int(state_info.x),int(state_info.y))
        t.write(answer)                                 #state_info.state.item()

print(notlist)
s.exitonclick()

''''
for i in range(49):
    answer = s.textinput(title = "%d/50 States correct",%i+1,prompt = "state name :")
    
    if answer not in datalist:
        i = i-1
    else:
        datalist.remove(answer)





turtle.mainloop()
'''