from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Score
import time


screen = Screen()
screen.bgcolor("black")
screen.title("Welcome to Pong!")
screen.setup(width=800, height=600)

game_is_on = True

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball(0, 0)
score = Score()


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

    #detect collision with upper/lower walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        score.increase_r_score()


    elif ball.distance(left_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()
        score.increase_l_score()


    #detect ball is out of bounds

    if ball.xcor() > 400 or ball.xcor() < -400:
        score.game_over()
        score.update_l_score()
        score.update_r_score()
        game_is_on = False








screen.exitonclick()