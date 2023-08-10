import string
import random
from tkinter import *

characters = string.printable


def generate():
    password_length = int(entry2.get())
    password = ""

    for _ in range(password_length):
        password += random.choice(characters)

    entry3.config(state="normal")
    entry3.delete(0, END)
    entry3.insert(0, password)
    entry3.config(state="readonly")


def reset():
    entry3.config(state="normal")
    entry3.delete(0, END)
    entry3.config(state="readonly")


def accept():
    text = entry3.get()
    if text:
        exit()


win = Tk()
win.geometry("800x700")
win.title("Password Generator")
canvas = Canvas(win, width=800, height=700, bg="black")
canvas.create_text(400, 70, text="Password Generator",
                   fill="white", font=("Bold", 40))

canvas.create_rectangle(80, 120, 700, 450, fill="white")

label1 = Label(canvas, text="Enter Username :", font=("Arial", 15),bg="white")
label1.place(x=120, y=220)
entry1 = Entry(canvas, font=("Arial", 15), width=33, border=3)
entry1.place(x=300, y=220)

label2 = Label(canvas, text="Password Length :", font=("Arial", 15),bg="white")
label2.place(x=120, y=280)
entry2 = Entry(canvas, font=("Arial", 15), width=33, border=3)
entry2.place(x=300, y=280)

label3 = Label(canvas, text="Generated\n Password :", font=("Arial", 15),bg="white")
label3.place(x=120, y=360)
entry3 = Entry(canvas, font=("Arial", 15), width=33, border=3)
entry3.place(x=300, y=370)
entry3.config(state="readonly")


# BUTTONS IN GUI
button_1 = Button(canvas, text='Generate', height=2, width=10, bg="white",
                  fg="black", font=("Arial", 15), borderwidth=3, command=generate)
button_1.place(x=150, y=500)

button_2 = Button(canvas, text='Accept', height=1, width=10,
                  bg="grey", fg="white", font=("Arial", 15), borderwidth=3, command=accept)
button_2.place(x=350, y=510)

button_3 = Button(canvas, text='Reset', height=1, width=10,
                  bg="grey", fg="white", font=("Arial", 15), borderwidth=3, command=reset)
button_3.place(x=500, y=510)

canvas.pack()


win.mainloop()