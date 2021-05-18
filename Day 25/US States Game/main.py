from turtle import Turtle, Screen
import pandas

#TODO: Create Turtle Screen that has the image as a bg and

screen = Screen()
state_image = Turtle()
image = "blank_states_img.gif"
screen.register_shape("blank_states_img.gif")
state_image.shape(image)

#TODO: Import the csv using PANDAS
data = pandas.read_csv("50_states.csv")
states = data["state"]


#TODO: Store user input and if it matches a "State" in the csv, create a TURTLE of that STATE NAME
# that will move tothe COORDS in x,y

game_is_on = True #setting game up
states_count = 0 #tracking correct states
already_guessed = [] #tracking guesses
state_dict = {
    "States"
}

while game_is_on == True:
    user_guess = screen.textinput(title="test input", prompt="Name a state! (or 'exit' to end the game)").title() #getting user input
    if data['state'].str.contains(user_guess).any() and user_guess not in already_guessed:
        #check answer again list of states and guessed list
        get_state_row = data[data.state == user_guess]
        state_text = Turtle()
        state_text.hideturtle()
        state_text.penup()
        state_text.shape("classic")
        state_text.goto(int(get_state_row.x), int(get_state_row.y))
        state_text.write(arg=user_guess, align="center", font=("Arial", 10))
        states_count += 1
        already_guessed.append(user_guess)

    if states_count >= 50: #if all states are guessed, displays Congrats message.
        state_text.goto(0, 0)
        state_text.write(arg="CONGRATS!", align="center", font=("Arial", 50))
        game_is_on = False

    if user_guess == "exit" or user_guess == "Exit":
        #creating way to exit and print missing states to csv
        missing_states = []
        for state in states:
            if state not in already_guessed:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break



screen.exitonclick()