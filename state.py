from turtle import Turtle
ALIGN ='center'
FONT = ('Arial', 9, 'normal')

class State(Turtle):
    def __init__(self, state, x, y):
        super().__init__()
        self.penup()
        self.goto(x, y)
        self.write(f"{state}", False, align=ALIGN, font=FONT)
        self.hideturtle()

