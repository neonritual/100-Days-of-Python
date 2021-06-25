import tkinter
window = tkinter.Tk()

window.title("My first GUI program!")
window.minsize(width=500, height=300)

#Layout Managers: Pack, Place, Grid

#pack() can be aligned left, right, center, but cannot be aligned to a specific location.

#place() is about precise positioning, uses an x and y value.

# my_label = tkinter.Label(text="THIS IS A LABEL ok", font=("Arial", 24, "bold"))
#
# my_label.place(x=100, y=100)

#Grid images the program as a grid, aka rows and columns, and allows u to position on row and column
#position, which will be relative to other grid calls


#CHALLENGE--- create layout according to teacher's image.


my_label = tkinter.Label(text="THIS IS A LABEL ok", font=("Arial", 24, "bold"))
my_label.grid(row=1, column=1)
button = tkinter.Button(text="CLICK me!", command=button_clicked)
button.pack()

#Entry (tkinter input)
entry = tkinter.Entry(textvariable="")
entry.pack()


window.mainloop()


