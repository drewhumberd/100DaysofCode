from turtle import Screen, Turtle
import pandas

turtle = Turtle()
screen = Screen()
screen.title("US States Game")
image = "supportfiles/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_data = pandas.read_csv("supportfiles/50_states.csv")
states_writer = Turtle()
states_writer.penup()
states_writer.hideturtle()
all_states = states_data.state.to_list()
guessed_states = []
def answer_checker():
    guessed_states.append(answer_state)
    for states in states_data.state:
        if answer_state == states:
            state_coords = states_data.loc[
                states_data.state == answer_state, ['x','y']
                ].values.flatten().tolist()
            state_x = state_coords[0]
            state_y = state_coords[1]
            states_writer.goto(state_x, state_y)
            states_writer.write(answer_state)
        elif answer_state is "Exit":
            break
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 correct", \
                                    prompt="What's a state name? Exit to quit").title()
    answer_checker()
screen.mainloop()
missed_states = [state for state in all_states if state not in guessed_states]
states_ser = pandas.DataFrame(missed_states)
states_ser.to_csv("missed_states.csv")