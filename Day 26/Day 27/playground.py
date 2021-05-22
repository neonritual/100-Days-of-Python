
#CHALLENGE--- create layout according to teacher's image.
import tkinter
window = tkinter.Tk()

window.title("My first GUI program!")
window.minsize(width=500, height=300)


my_label = tkinter.Label(text="THIS IS A LABEL ok", font=("Arial", 24, "bold"))
my_label.grid(row=1, column=1)
my_label.config(padx=5, pady=50)

button1 = tkinter.Button(text="HELLO")
button1.grid(row=2, column=2)
button1.config(padx=50, pady=50)

button2 = tkinter.Button(text="HELLO")
button2.grid(row=1, column=3)
button2.config(padx=50, pady=50)

entry = tkinter.Entry(textvariable="")
entry.grid(row=3, column=3)




window.mainloop()






#Challenge: make a function called add(), that will always add ALL the arguments within it.
#
# def add(*args):
#     answer = sum(args)
#     print(answer)

# add(50, 50, 50, 50, 50, 50)