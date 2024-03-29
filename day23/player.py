from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.return_to_start()
        self.setheading(90)

    def move(self):
        cur_x = self.xcor()
        cur_y = self.ycor()
        self.goto(cur_x, cur_y + MOVE_DISTANCE)
    
    def return_to_start(self):
        self.goto(STARTING_POSITION)

    def check_at_end(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
