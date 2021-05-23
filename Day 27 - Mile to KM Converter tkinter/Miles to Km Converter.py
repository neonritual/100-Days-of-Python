#Create a Miles to km converter in tkinter.
#3 rows, 3 column design.
#             #  entry              ## miles
# is equal to # ## OUTPUT           ### Km
#              # Calculate Button ###


import tkinter

window = tkinter.Tk() #making a winter

window.title("Miles to Kilometers Converter")
window.minsize(width=100, height=100)
window.config(padx=10, pady=10)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)

km_label = tkinter.Label(text="Km")
km_label.grid(row=1, column=2)

equal_label = tkinter.Label(text="is equal to")
equal_label.grid(row=1, column=0)

user_input = tkinter.Entry(width=7, textvariable="")
user_input.grid(row=0, column=1)

answer_label = tkinter.Label(text="")
answer_label.grid(row=1, column=1)

def calculate():
    answer = int(user_input.get()) * 1.609344
    answer_label.config(text=answer)

calc_button = tkinter.Button(text="Calculate", command=calculate)
calc_button.grid(row=2, column=1)



window.mainloop()