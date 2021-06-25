from turtle import Turtle, Screen
import time
from player import Player
from car_manager import CarManager, car_list
from scoreboard import Scoreboard

FINISH_LINE_Y = 280
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("TURTLE CROSSING")

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()




#TODO: Create turtle that starts at bottom, listens for the UP key and moves upwards. (step 3)
screen.listen()
screen.onkey(player.move_player, "Up")


loop_count = 6



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.move_cars()
    screen.update()
    loop_count -= 1
    if loop_count == 0:
        car_manager.new_car()
        loop_count = 6


#TODO: Detect when the turtle player collides with a car and stop the game if this happens. (step 5)

    for x in car_list:
        if x.distance(player) <= 20:
            scoreboard.game_over()
            game_is_on = False

#TODO: Detect when the turtle player has reached the top (FINISH_LINE_Y). When this happens,
# return turtle to start and increase speed of cards. (hint: maybe create an attibute and using the
# MOVE_INCREMENT to increase car speed.) (step 6)

    # TODO: Create scoreboard that keeps track of the users level. When the turtle hits a car,
    # GAME OVER should be displayed in the middle. (step 7)

    if player.ycor() >= 280:
        car_manager.speed_up()
        player.return_to_start()
        scoreboard.increase_score()








screen.exitonclick()