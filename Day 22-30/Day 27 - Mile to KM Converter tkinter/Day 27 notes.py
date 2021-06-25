import tkinter

#Tkinter is a GUI built into Python.

window = tkinter.Tk() #making a winter
# window.mainloop() #a built-in loop that keeps the generated window active.
#BUT this MUST be at the end of the code!!

window.title("My first GUI program!")
window.minsize(width=500, height=300) #this sets the minimum size, but the window can be resized and will scale

#LABEL

my_label = tkinter.Label(text="I am a Label!", font=("Arial", 24)) #creates a label, but doesnot display it.
my_label.pack() #this "packs" the label, or displays in the middle.
#You can change values like a dict:
#   my_label["text"] = "New Text"
#Or using built in "config"
my_label.config(text="Configgy")

def button_clicked():
    my_label.config(text=entry.get())

button = tkinter.Button(text="CLICK me!", command=button_clicked)
button.pack()

#Entry (tkinter input)
entry = tkinter.Entry(textvariable="")
entry.pack()

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()


#-----------------

###Arguments with Default Values
#when you define a function, you can specify default values.
#ex. def my_function(a=1, b=2, c=3)
#Those beome the default a, b, and c values for that function, and you can run
#my_function() without specifying anything and it will assume that.
#But, if you DO want to change one, you CAN specify, even just one value
#ex. my_function(b=5)

###Unlimited Arguments
#you can make argument unlimitd by using
#      *args
#this is not set in stone btw, it's just the most commonly used way to type it
#cause args = arguments, the asterisk is the important one

#for example, def my_function(a, b) only allows for two
#but defv my_function(*args) allows for many

#There is also **kwargs, which allows unlimited KEYWORD arguments
#
# def calculate(**kwargs):
#     print(kwargs)
#
#
# calculate(add=3, multiply=5) ##this creates a DICTIONARY with keys of add and multiply, and values of 3 and 5
#
#
#
# def calculate(n, **kwargs):
#     print(kwargs)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#     ###This will take the value of n, and then add it to the value in "add", and multiply it by the value in "multiply"
#

#####USING .GET
#When making a function, you can use .get to create an arg that doesnot NEED to have a value, making them OPTIONAL.
# Ex.:
# class Car:
#     def __init__(self, **kwargs):
#         self.make = kwargs.get("make")
#         self.model = kwargs.get("model")
#         #this sets up two arguments but you do not NEED them, if they don't exist it will return None.
#         #These key arguments are all OPTIONAL
#
#
#
# calculate(add=3, multiply=5) ##this creates a DICTIONARY with keys of add and multiply, and values of 3 and 5
#
#

window.mainloop()