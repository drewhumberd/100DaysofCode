from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCORE_POS = (-280, 250)

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(SCORE_POS)
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def score_up(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("G A M E O V E R", align="center", font=FONT)