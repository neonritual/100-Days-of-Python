from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.setheading(90)
        self.penup()
        self.turtlesize(1, 5)
        self.goto(x, y)
        self.color("white")

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)