from turtle import Turtle, Screen
import time
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

turtle = Player()
screen.onkeypress(turtle.move_player(), "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()



#TODO: Create turtle that starts at bottom, listens for the UP key and moves upwards. (step 3)
#TODO: Create Cars 20px by 40px randomly generated along the y axis and move to the left of the screen.
# No cars should be generated in the top and bottom 50px of the screen (hint: gen new car only every
# 6th time the game loop runs.) (step 4 vid)
#TODO: Detect when the turtle player collides with a car and stop the game if this happens. (step 5)
#TODO: Detect when the turtle player has reached the top (FINISH_LINE_Y). When this happens,
# return turtle to start and increase speed of cards. (hint: maybe create an attibute and using the
# MOVE_INCREMENT to increase car speed.) (step 6)
#TODO: Create scoreboard that keeps track of the users level. When the turtle hits a car,
# GAME OVER should be displayed in the middle. (step 7)