from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):
    '''defines scoreboard at top of game window'''
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("day20/data.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setpos(0, 280)
        self.write_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        with open("day20/data.txt", "w") as file:
            file.write(str(self.highscore))
        self.score = 0
        self.write_score()

    def write_score(self):
        '''prints current score'''
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGN, font=FONT)

    # def game_over(self):
    #     '''prints GAME OVER'''
    #     self.setpos(0,0)
    #     self.write("GAME OVER", align=ALIGN, font=FONT)

    def score_go_up(self):
        '''increments score'''
        self.score +=1
        self.write_score()
