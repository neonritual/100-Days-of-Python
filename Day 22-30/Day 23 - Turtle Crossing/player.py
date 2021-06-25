from turtle import Turtle
from car_manager import CarManager
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.turtlesize(1, 1)
        self.goto(STARTING_POSITION)
        self.color("green")
    def move_player(self):
        self.forward(10)
    def return_to_start(self):
        self.goto(STARTING_POSITION)





