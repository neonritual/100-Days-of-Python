#################################
######PRACTICE: using Turtle, importing from other pages
##################################

import another_module
print(another_module.testing)

from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("Coral")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight) #Screen is an object, and canvheight is an attribute associated with it.
my_screen.exitonclick() #this Method (of Screen) lets it run until you click.

