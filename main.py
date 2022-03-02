import turtle
import pandas
from state import State
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.setup(830, 600)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
score_board = Scoreboard()
correct_states = []
all_states = data.state.to_list()

while len(correct_states) < 50:
    answer_state = screen.textinput(title="Guess the state",
                                    prompt="What's another state name?").title()
    if answer_state == "Exit":
        missing_states = [state for  state in all_states if state not in correct_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break


    if answer_state not in correct_states:
        print(answer_state)
        #print(data[data.state == answer_state])

        state = data[data.state == answer_state]
        print(state.state.item())
        x = int(data[data.state == answer_state].x)
        print(x)
        y = int(data[data.state == answer_state].y)
        print(y)

        name_state = State(state.state.item(), x, y)
        score_board.update_score()
        correct_states.append(answer_state)
        print(correct_states)
    else:
        None

#states_to_learn.csv

screen.mainloop()