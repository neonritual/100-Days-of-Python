from turtle import Turtle

x = 0
y = 0

class Ball(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("circle")
        self.speed("fast")
        self.penup()
        self.turtlesize(1, 1)
        self.goto(x, y)
        self.color("white")

    def move_it(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)



