from turtle import Turtle, Screen
from paddles import Paddle


screen = Screen()
screen.bgcolor("black")
screen.title("Welcome to Pong!")
screen.setup(width=800, height=600)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)

screen.listen()

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")


screen.exitonclick()