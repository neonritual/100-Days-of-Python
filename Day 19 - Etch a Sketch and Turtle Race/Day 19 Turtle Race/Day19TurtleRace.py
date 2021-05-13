from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput("Make your bets!", "What turtle do you think will win? Enter a color:   ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
all_turtles = []

start_ys = [-70, -40, -10, 20, 50, 80]
for turtle_index in range (0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=start_ys[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The winning color was {winning_color}.")
            else:
                print(f"Sorry, the winning color was {winning_color}.")
        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)











screen.exitonclick()