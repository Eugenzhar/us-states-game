from turtle import Turtle
ALIGN ='center'
FONT = ('Arial', 14, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = -1
        self.penup()
        self.goto(0, 250)
        self.write(f"{self.score}/50", False, align=ALIGN, font=FONT)
        self.update_score()


    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}/50", False, align=ALIGN, font=FONT)

