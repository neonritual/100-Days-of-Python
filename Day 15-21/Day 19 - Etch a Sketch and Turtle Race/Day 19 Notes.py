#TODO: EVENT LISTENERS

#Allows program to "listen" to user,
# for example by user clicks,

from turtle import Turtle, Screen
tu = Turtle()
screen = Screen()

#Next we need to make a call so that the screen
# starts "listening" when a particular key is pressed.
screen.listen()

#to bind a key to this, we need to use an event listener.
#we will use turtle.onkey, which req. a function and a key.

def move_forwards():
    tu.forward(10)

screen.onkey(fun=move_forwards, key="space") ##when calling
# a function here, we don"t use the () or else it will START it.



screen.exitonclick()