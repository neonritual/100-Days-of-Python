from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

title = Label(text="Timer", bg=YELLOW, fg="green", font=(FONT_NAME, 50, "bold"))
title.grid(row=1, column=2)

start_button = Button(text="Start")
start_button.grid(row=3, column=1)

reset_button = Button(text="Reset")
reset_button.grid(row=3, column=3)

check_mark = Label(text="✓", bg=YELLOW, fg="green", font=(FONT_NAME, 30, "bold"))
check_mark.grid(row=4, column=2)

# fg＝GREEN


window.mainloop()