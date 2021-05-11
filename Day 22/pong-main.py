from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
import time


screen = Screen()
screen.bgcolor("black")
screen.title("Welcome to Pong!")
screen.setup(width=800, height=600)

game_is_on = True

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball(0, 0)

screen.listen()

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_it()

ball.move_it()


screen.exitonclick()