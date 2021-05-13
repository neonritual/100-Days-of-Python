from turtle import Turtle
import time

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
        self.x_move = 10
        self.y_move = 10

    def move_it(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1



    # def bounce_down(self):
    #     time.sleep(0.1)
    #     new_y = self.ycor() - 10
    #     new_x = self.xcor() + 10
    #     self.goto(new_x, new_y)
    #     self.bounce_down()
    #
    # def bounce_up(self):
    #     time.sleep(0.1)
    #     new_y = self.ycor() + 10
    #     new_x = self.xcor() - 10
    #     self.goto(new_x, new_y)
    #     self.bounce_up()






