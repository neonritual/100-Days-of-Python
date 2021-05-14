from turtle import Turtle, Screen
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
game_is_on = True
screen = Screen()


#TODO: Create Cars 20px by 40px randomly generated along the y axis and move to the left of the screen.
# No cars should be generated in the top and bottom 50px of the screen (hint: gen new car only every
# 6th time the game loop runs.) (step 4 vid)
cars = []

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.make_cars()
        self.hideturtle()

    def make_cars(self):
        for _ in range(10):
            random_y = random.randint(-200, 250)
            random_x = random.randint(-200, 250)
            self.car = Turtle()
            self.car.penup()
            self.car.color(random.choice(COLORS))
            self.car.shape("square")
            self.car.shapesize(1, 2)
            self.car.goto(random_x, random_y)
            cars.append(self.car)
            random_x = random.randint(-200, 250)
            random_y = random.randint(-200, 250)


    def move_cars(self):
        for turtle in cars:
            time.sleep(0.01)
            turtle.setheading(180)
            turtle.forward(10)

    def new_car(self):
        random_y = random.randint(-250, 250)
        self.car = Turtle()
        self.car.penup()
        self.car.color(random.choice(COLORS))
        self.car.shape("square")
        self.car.shapesize(1, 2)
        self.car.goto(400, random_y)
        cars.append(self.car)



