import turtle
import pandas
from state import State

screen = turtle.Screen()
screen.setup(830, 600)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")


printed_states =[]
game_on = True
while game_on :
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state name?")
    print(answer_state)
    #print(data[data.state == answer_state])

    state = (data[data.state == answer_state])
    print(str(state.state))
    x = int(data[data.state == answer_state].x)
    print(x)
    y = int(data[data.state == answer_state].y)
    print(y)

    name_state = State(answer_state, x, y)

screen.mainloop()