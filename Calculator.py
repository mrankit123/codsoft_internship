from tkinter import *


def insert(val):
    index = entry.index(INSERT)
    entry.insert(index, val)


def solve():
    s = entry.get()
    result = eval(s)

    entry.delete(0, END)
    entry.insert(END, result)


def remove_one():
    ind = entry.index(INSERT)
    entry.delete(ind-1, ind)


win = Tk()
win.geometry("400x600")
win.title("Calculator")

canvas = Canvas(win, width=400, height=600, bg="grey")

entry = Entry(canvas, font=("Arial", 26), width=20, border=0, bg="black",
              fg="white", insertontime=500, insertbackground="white", justify="right")
entry.place(x=10, y=70)

line = canvas.create_line(15, 120, 385, 120, fill="black", width=1)



buttons = [
    ("AC", lambda: entry.delete(0, END)),
    ("^", lambda: insert("**")),
    ("÷", lambda: insert("/")),
    ("x", remove_one),

    ("7", lambda: insert(7)),
    ("8", lambda: insert(8)),
    ("9", lambda: insert(9)),
    ("*", lambda: insert("*")),

    ("4", lambda: insert(4)),
    ("5", lambda: insert(5)),
    ("6", lambda: insert(6)),
    ("-", lambda: insert("-")),

    ("1", lambda: insert(1)),
    ("2", lambda: insert(2)),
    ("3", lambda: insert(3)),
    ("+", lambda: insert("+")),

    ("π", lambda: insert(3.14)),
    ("0", lambda: insert(0)),
    (".", lambda: insert(".")),
    ("=", solve)
]

x_pos = 10
y_pos = 150
color = "orange red"
l = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
for label, command in buttons:
    if label in l:
        color = "white"
    else:
        color = "orange red"
    Button(win, text=label, height=1, width=4, bg="black", fg=color,
           font=("Arial", 25), borderwidth=0, command=command).place(x=x_pos, y=y_pos)
    x_pos += 99
    if x_pos > 307:
        x_pos = 10
        y_pos += 90


canvas.pack()

win.mainloop()