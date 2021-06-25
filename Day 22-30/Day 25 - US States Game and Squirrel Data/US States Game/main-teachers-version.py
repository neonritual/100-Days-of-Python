import pandas
from turtle import Turtle, Screen

#TODO: Create Turtle Screen that has the image as a bg and

screen = Screen()
state_image = Turtle()
image = "blank_states_img.gif"
screen.register_shape("blank_states_img.gif")
state_image.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"States Guessed: {len(guessed_states)}/50",
                                    prompt="What's another state's name?").title()
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()