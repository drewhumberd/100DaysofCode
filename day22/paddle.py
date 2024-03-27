from turtle import Turtle

LEFT_START_POS = (-360, 0)
RIGHT_START_POS = (360, 0)
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.resizemode("user")
        self.setheading(90)
        self.shapesize(1,5,0)
        self.penup()
        if side == "left":
            self.setpos(LEFT_START_POS)
        elif side == "right":
            self.setpos(RIGHT_START_POS)

    def up(self):
        if self.ycor() < 280:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -280:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)
