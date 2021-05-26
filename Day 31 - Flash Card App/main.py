import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.title("Flash Cards")
window.config(padx=50, pady=20)
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
window.config(bg=BACKGROUND_COLOR)


#--------CSV Stuff -----------#

#name dict of french words and translations
new_dict = pd.read_csv("./data/french_words.csv").to_dict(orient="records")


#------- Inserting New French Word -----#
new_french_word = {} #blank dicr to store current card

def new_word(): #gen new card, display it, stop timer at start and then restart after display
    global new_french_word, flip_time
    window.after_cancel(flip_time)
    new_french_word = random.choice(new_dict)
    canvas.itemconfig(bg_image, image=card_front)
    canvas.itemconfig(french_word, text=new_french_word["French"], fill="black")
    canvas.itemconfig(what_language, text="French")
    flip_time = window.after(3000, flip_card)


def flip_card(): #turn card over and show English
    canvas.itemconfig(bg_image, image=card_back)
    canvas.itemconfig(french_word, text=new_french_word["English"], fill="white")
    canvas.itemconfig(what_language, text="English")

flip_time = window.after(3000, flip_card)

#------ Flip to English ------#







#---------- UI Stuff -----------#
card_front = tk.PhotoImage(file="./images/card_front.png")
card_back = tk.PhotoImage(file="./images/card_back.png")
batsu_button = tk.PhotoImage(file="./images/wrong.png")
maru_button = tk.PhotoImage(file="./images/right.png")


bg_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=1, column=1, columnspan=2)

what_language = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
french_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

new_word()


#
no_button = tk.Button(image=batsu_button, highlightthickness=0, command=new_word)
no_button.grid(row=2, column=1)
yes_button = tk.Button(image=maru_button, highlightthickness=0, command=new_word)
yes_button.grid(row=2, column=2)



canvas.mainloop()



