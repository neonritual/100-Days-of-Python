from turtle import Turtle, Screen
import random
# #you can import everything using the *
# #from turtle import * #but this can make it confusing when you don't know where everything is coming from.
#import turtle as t
#you can also import modules AS something, to for example shorten a super long name.

#Some modules need to be Installed. Only built-in python packages/modules can just be "imported' easily like
# that. Some packages you need to install FIRST before importing.


tulip = Turtle()

tulip.shape("turtle")
tulip.color("salmon")

# #Challenge: draw a square.
# for _ in range(4):
#     tulip.right(90)
#     tulip.forward(100)

#Challenge: draw a dashed line:
# for _ in range(10):
#     tulip.forward(10)
#     tulip.penup()
#     tulip.forward(10)
#     tulip.pendown()

#Challenge: Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon.
#all 100 in terms of length.

# colors = ["red", "black", "green", "yellow", "orange", "purple", "brown"]
# def draw_shapes(sides):
#     angle = 360 / sides
#     for _ in range(sides):
#         tulip.forward(100)
#         tulip.right(angle)
#
#
# for shapes_sides in range(3, 11):
#         draw_shapes(shapes_sides)
#         tulip.color(random.choice(colors))

#Challenge: Draw a random Walk
# colors = ["red", "black", "green", "yellow", "orange", "purple", "brown"
#           ]
# tulip.pensize(10)
# draw_range = random.randrange(1, 100)
# print(draw_range)
# for _ in range(draw_range):
#     tulip.forward(random.randrange(1, 100))
#     tulip.right(random.randrange(1, 100))
#     tulip.color(random.choice(colors))

####OR:
# colors = ["red", "black", "green", "yellow", "orange", "purple", "brown"]
# direction = [0, 90, 180, 270]
# tulip.pensize(10)
# tulip.speed("fastest")
# for _ in range(200):
#     tulip.color(random.choice(colors))
#     tulip.forward(30)
#     tulip.setheading(random.choice(direction))

#TODO: WHAT IS A TUPLE?
# #A datatype with round brackets, with insides separated by commas ,
# my_tuple(1, 2, 3)
# my_tuple[2] ## this equals 3
#UNLIKE A LIST, a tuple can NOT be CHANGED!

#How to get a random color:
#firs,t gotta open up the colormode in Turtle to allow for it:


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color_tuple = (r, b, g)
#     return color_tuple
# turtle.colormode(255)
# direction = [0, 90, 180, 270]
# tulip.pensize(10)
# tulip.speed("fastest")
# for _ in range(200):
#     tulip.color(random_color())
#     tulip.forward(30)
#     tulip.setheading(random.choice(direction))


#Challenge: make a spirograph!
tulip.speed("fastest")
colors = ["RosyBrown3", "RosyBrown1", "RosyBrown2", "RosyBrown3"]
def draw_spirograph(gap_size):
    for _ in range (int(360 / gap_size)):
        tulip.circle(100)
        current_heading = tulip.heading()
        tulip.setheading(current_heading + gap_size)
    tulip.color(random.choice(colors))

draw_spirograph(5)













screen = Screen()
screen.exitonclick()