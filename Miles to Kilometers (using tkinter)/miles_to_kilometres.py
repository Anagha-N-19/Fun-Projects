import tkinter
from PIL import Image, ImageTk
from tkinter import ttk

window = tkinter.Tk()
bg= ImageTk.PhotoImage(file="newroad.jpg")

canvas= tkinter.Canvas(window,width= 300, height= 300)
canvas.pack(expand=True)
canvas.create_image(0,0,image=bg, anchor="nw")
window.title("Miles to Kilometers converter")


window.minsize(width=300, height=300)
my_label = tkinter.Label(text="Miles to Kilometers", font=("Times New Roman", 15, "bold"))
my_label.place(x=90, y=20)


def button_click():
    kilm = round(1.609344 * float(input_data.get()), 2)
    new_label = tkinter.Label(text=f"{kilm} kilometers", font=("Times New Roman", 14, "bold"))
    new_label.place(x=90, y=200)


# Entry
input_data = tkinter.Entry(width=10)
input_data.place(x=120, y=80)

button = tkinter.Button(text="Convert", command=button_click)
button.place(x=128, y=160)

window.mainloop()
