#TODO: Create a dot painting with 10 by 10 rows of spots.
#Dots 20 in size, and 50 spaced between,

from turtle import Turtle, Screen
import random



# color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135),
#                 (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71),
#                (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164),
#                 (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74),
#                 (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153),
#                 (174, 94, 97), (176, 192, 209)]

color_list = ["orange", "yellow", "light blue", "light green"]

tulip = Turtle()


#TODO: Create a dot painting with 10 by 10 rows of spots.
#Dots 20 in size, and 50 spaced between,

tulip.speed("fastest")
tulip.penup()
tulip.bk(300)
tulip.left(90)
tulip.forward(270)

# tulip.dot(20, random.choice(color_list))
# tulip.right(90)
# for _ in range(12):
#     tulip.forward(50)
#     tulip.dot(20, random.choice(color_list))


tulip.right(90)
tulip.forward(50)
for _ in range(10):
    tulip.dot(20, random.choice(color_list))
    tulip.forward(50)
for _ in range(10):
    tulip.back(500)
    tulip.right(90)
    tulip.forward(50)
    tulip.left(90)
    for _ in range(10):
        tulip.dot(20, random.choice(color_list))
        tulip.forward(50)














screen = Screen()
screen.exitonclick()